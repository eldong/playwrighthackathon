@description('The Azure region for the Cosmos DB account')
param location string

@description('The name of the Cosmos DB account')
param cosmosDbAccountName string

@description('The name of the Cosmos DB database')
param cosmosDbDatabaseName string

module cosmosDb 'br/public:avm/res/document-db/database-account:0.19.0' = {
  params: {
    name: cosmosDbAccountName
    location: location
    disableLocalAuthentication: true
    networkRestrictions: {
      publicNetworkAccess: 'Enabled'
    }
    sqlDatabases: [
      {
        name: cosmosDbDatabaseName
      }
    ]
  }
}

output endpoint string = cosmosDb.outputs.endpoint
output name string = cosmosDb.outputs.name
output resourceId string = cosmosDb.outputs.resourceId
