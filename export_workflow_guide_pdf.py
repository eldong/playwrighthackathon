#!/usr/bin/env python3
"""
Export the Copilot Workflow Guide markdown file to PDF format.
Requires: markdown2 and either weasyprint or reportlab
"""

import sys
from pathlib import Path

try:
    # Try using markdown2 + weasyprint
    from markdown2 import markdown
    from weasyprint import HTML, CSS
    import tempfile
    
    project_root = Path(__file__).parent
    output_dir = project_root / 'docs'
    output_dir.mkdir(exist_ok=True)
    input_file = project_root / 'copilot-workflow-guide.md'
    output_file = output_dir / 'copilot-workflow-guide.pdf'
    
    # Read markdown
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to HTML
    html_content = markdown(md_content, extras=['tables', 'fenced-code-blocks'])
    
    # Wrap in HTML document with styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Calibri', 'Arial', sans-serif; margin: 1in; line-height: 1.6; }}
            h1 {{ font-size: 24px; margin-top: 1em; margin-bottom: 0.5em; }}
            h2 {{ font-size: 18px; margin-top: 0.8em; margin-bottom: 0.4em; }}
            h3 {{ font-size: 14px; margin-top: 0.6em; margin-bottom: 0.3em; }}
            code {{ background-color: #f4f4f4; padding: 2px 4px; font-family: 'Courier New', monospace; }}
            pre {{ background-color: #f4f4f4; padding: 10px; overflow-x: auto; border-radius: 4px; }}
            table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #4472C4; color: white; }}
            blockquote {{ border-left: 4px solid #4472C4; padding-left: 1em; margin-left: 0; color: #666; font-style: italic; }}
            ul, ol {{ margin: 0.5em 0; }}
            li {{ margin: 0.3em 0; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Convert HTML to PDF
    HTML(string=full_html).write_pdf(output_file)
    print(f"✓ Created {output_file}")
    
except ImportError as e:
    print(f"Required library not found: {e}")
    print("Attempting alternative method...")
    
    # Fallback: try using reportlab
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        import re
        
        project_root = Path(__file__).parent
        output_dir = project_root / 'docs'
        output_dir.mkdir(exist_ok=True)
        input_file = project_root / 'copilot-workflow-guide.md'
        output_file = output_dir / 'copilot-workflow-guide.pdf'
        
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        doc = SimpleDocTemplate(str(output_file), pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom styles
        title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, spaceAfter=12, textColor=colors.HexColor('#1F4E78'))
        heading2_style = ParagraphStyle('CustomHeading2', parent=styles['Heading2'], fontSize=14, spaceAfter=10, textColor=colors.HexColor('#1F4E78'))
        
        lines = md_content.split('\n')
        for line in lines:
            line_stripped = line.strip()
            
            if line_stripped.startswith('# '):
                story.append(Paragraph(line_stripped[2:], title_style))
                story.append(Spacer(1, 0.2*inch))
            elif line_stripped.startswith('## '):
                story.append(Paragraph(line_stripped[3:], heading2_style))
                story.append(Spacer(1, 0.1*inch))
            elif line_stripped.startswith('### '):
                story.append(Paragraph(line_stripped[4:], styles['Heading3']))
                story.append(Spacer(1, 0.08*inch))
            elif line_stripped.startswith('- '):
                story.append(Paragraph(line_stripped[2:], styles['BodyText']))
            elif line_stripped:
                story.append(Paragraph(line_stripped, styles['BodyText']))
            else:
                story.append(Spacer(1, 0.1*inch))
        
        doc.build(story)
        print(f"✓ Created {output_file}")
    
    except ImportError as e2:
        print(f"Alternative library also not available: {e2}")
        print("PDF libraries not installed. The DOCX file has been created successfully.")
        sys.exit(1)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
