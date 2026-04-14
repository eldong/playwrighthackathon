targetScope = 'resourceGroup'

@description('The Azure region for all resources')
param location string = resourceGroup().location

@description('A unique suffix for resource names')
param resourceNameSuffix string = uniqueString(resourceGroup().id)

@description('The name of the App Service Plan')
param appServicePlanName string = 'plan-${resourceNameSuffix}'

@description('The name of the Web App')
param webAppName string = 'app-${resourceNameSuffix}'

@description('The name of the Cosmos DB account')
param cosmosDbAccountName string = 'cosmos-${resourceNameSuffix}'

@description('The name of the Cosmos DB database')
param cosmosDbDatabaseName string = 'appdb'

@description('The SKU of the App Service Plan')
param appServicePlanSku string = 'B1'

// App Service Plan
module appServicePlan 'br/public:avm/res/web/serverfarm:0.7.0' = {
  params: {
    name: appServicePlanName
    location: location
    kind: 'linux'
    reserved: true
    skuName: appServicePlanSku
    skuCapacity: 1
  }
}

// Web App
module webApp 'br/public:avm/res/web/site:0.22.0' = {
  params: {
    name: webAppName
    location: location
    kind: 'app,linux'
    serverFarmResourceId: appServicePlan.outputs.resourceId
    managedIdentities: {
      systemAssigned: true
    }
    siteConfig: {
      linuxFxVersion: 'DOTNETCORE|8.0'
      minTlsVersion: '1.2'
      ftpsState: 'Disabled'
    }
    httpsOnly: true
  }
}

// Set app settings separately to avoid circular dependency with Cosmos DB
resource webAppSettings 'Microsoft.Web/sites/config@2023-12-01' = {
  name: '${webAppName}/appsettings'
  properties: {
    CosmosDb__Endpoint: cosmosDb.outputs.endpoint
  }
  dependsOn: [webApp]
}

// Cosmos DB account with SQL database
module cosmosDb 'modules/cosmosdb.bicep' = {
  params: {
    location: location
    cosmosDbAccountName: cosmosDbAccountName
    cosmosDbDatabaseName: cosmosDbDatabaseName
  }
}

// Cosmos DB data-plane role assignment — separate to break the circular dependency
resource cosmosDbAccount 'Microsoft.DocumentDB/databaseAccounts@2024-05-15' existing = {
  name: cosmosDbAccountName
}

resource cosmosDbRoleAssignment 'Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments@2024-05-15' = {
  name: guid(cosmosDbAccountName, webAppName, '00000000-0000-0000-0000-000000000002')
  parent: cosmosDbAccount
  properties: {
    principalId: webApp.outputs.systemAssignedMIPrincipalId
    roleDefinitionId: '${cosmosDbAccount.id}/sqlRoleDefinitions/00000000-0000-0000-0000-000000000002'
    scope: cosmosDbAccount.id
  }
  dependsOn: [cosmosDb]
}

output webAppUrl string = 'https://${webApp.outputs.defaultHostname}'
output webAppName string = webApp.outputs.name
output cosmosDbEndpoint string = cosmosDb.outputs.endpoint
