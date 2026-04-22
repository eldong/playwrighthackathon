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
        code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', fontSize=9, leftIndent=20, rightIndent=20, backColor=colors.HexColor('#F4F4F4'))

        def build_styled_table(table_rows):
            if len(table_rows) <= 1:
                return None

            # Remove markdown separator row like: |---|---| if present.
            separator_row = table_rows[1] if len(table_rows) > 1 else []
            if separator_row and all(cell and set(cell) <= {'-', ':'} for cell in separator_row):
                table_rows = [table_rows[0]] + table_rows[2:]

            if len(table_rows) <= 1:
                return None

            column_count = max(len(row) for row in table_rows)
            if column_count == 0:
                return None

            header_cell_style = ParagraphStyle(
                'TableHeaderCell',
                parent=styles['BodyText'],
                fontName='Helvetica-Bold',
                fontSize=9,
                textColor=colors.whitesmoke,
                leading=11,
            )
            body_cell_style = ParagraphStyle(
                'TableBodyCell',
                parent=styles['BodyText'],
                fontSize=8,
                leading=10,
            )

            normalized_rows = []
            for row_index, row in enumerate(table_rows):
                padded = list(row) + [''] * (column_count - len(row))
                cell_style = header_cell_style if row_index == 0 else body_cell_style
                normalized_rows.append([
                    Paragraph(cell if cell else ' ', cell_style) for cell in padded
                ])

            # Force table to fit the printable page width.
            col_width = doc.width / column_count
            table = Table(
                normalized_rows,
                colWidths=[col_width] * column_count,
                hAlign='LEFT',
                repeatRows=1,
            )
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
                ('LEFTPADDING', (0, 0), (-1, -1), 5),
                ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            return table

        lines = md_content.split('\n')
        in_table = False
        table_data = []

        i = 0
        while i < len(lines):
            line = lines[i]
            line_stripped = line.strip()

            # Parse markdown tables before other line handling.
            if line_stripped.startswith('|'):
                if not in_table:
                    in_table = True
                    table_data = []

                cells = [cell.strip() for cell in line_stripped.split('|')[1:-1]]
                if cells:
                    table_data.append(cells)

                i += 1
                continue
            elif in_table:
                table = build_styled_table(table_data)
                if table is not None:
                    story.append(table)
                    story.append(Spacer(1, 0.2*inch))

                in_table = False
                table_data = []

            if line_stripped.startswith('# '):
                story.append(Paragraph(line_stripped[2:], title_style))
                story.append(Spacer(1, 0.2*inch))
            elif line_stripped.startswith('## '):
                story.append(Paragraph(line_stripped[3:], heading2_style))
                story.append(Spacer(1, 0.1*inch))
            elif line_stripped.startswith('### '):
                story.append(Paragraph(line_stripped[4:], styles['Heading3']))
                story.append(Spacer(1, 0.08*inch))
            elif line_stripped.startswith('#### '):
                story.append(Paragraph(line_stripped[5:], styles['Heading4']))
                story.append(Spacer(1, 0.05*inch))
            elif line_stripped == '---':
                story.append(Spacer(1, 0.15*inch))
            elif line_stripped.startswith('```'):
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i])
                    i += 1
                if code_lines:
                    story.append(Paragraph('\n'.join(code_lines).strip(), code_style))
                    story.append(Spacer(1, 0.1*inch))
            elif line_stripped.startswith('> '):
                quote_text = line_stripped[2:].strip()
                quote_style = ParagraphStyle('Quote', parent=styles['Normal'], leftIndent=30, textColor=colors.HexColor('#666666'))
                story.append(Paragraph(f"<i>{quote_text}</i>", quote_style))
                story.append(Spacer(1, 0.08*inch))
            elif line_stripped.startswith('- '):
                story.append(Paragraph(f"• {line_stripped[2:].strip()}", ParagraphStyle('Bullet', parent=styles['Normal'], leftIndent=20)))
            elif re.match(r'^\d+\.\s', line_stripped):
                match = re.match(r'^(\d+)\.\s(.*)', line_stripped)
                if match:
                    story.append(Paragraph(f"{match.group(1)}. {match.group(2).strip()}", ParagraphStyle('Numbered', parent=styles['Normal'], leftIndent=20)))
            elif line_stripped:
                story.append(Paragraph(line_stripped, styles['BodyText']))
            else:
                story.append(Spacer(1, 0.05*inch))

            i += 1

        # If file ended while in a table, flush it.
        if in_table and len(table_data) > 1:
            table = build_styled_table(table_data)
            if table is not None:
                story.append(table)
                story.append(Spacer(1, 0.2*inch))
        
        doc.build(story)
        print(f"✓ Created {output_file}")
    
    except ImportError as e2:
        print(f"Alternative library also not available: {e2}")
        print("PDF libraries not installed. The DOCX file has been created successfully.")
        sys.exit(1)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
