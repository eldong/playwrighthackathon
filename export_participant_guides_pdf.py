#!/usr/bin/env python3
"""
Convert one or more participant guide markdown files to PDF format.
"""

import sys
from pathlib import Path

try:
    from markdown2 import markdown
    import tempfile
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    import re
    
    def md_to_pdf(markdown_file, output_file=None):
        """Convert markdown file to PDF document."""
        
        if output_file is None:
            project_root = Path(__file__).parent
            output_dir = project_root / 'docs'
            output_dir.mkdir(exist_ok=True)
            output_file = output_dir / f"{Path(markdown_file).stem}.pdf"
        
        with open(markdown_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        doc = SimpleDocTemplate(str(output_file), pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom styles
        title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, spaceAfter=12, textColor=colors.HexColor('#1F4E78'))
        heading2_style = ParagraphStyle('CustomHeading2', parent=styles['Heading2'], fontSize=14, spaceAfter=10, textColor=colors.HexColor('#1F4E78'))
        code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', fontSize=9, leftIndent=20, rightIndent=20, backColor=colors.HexColor('#F4F4F4'))
        
        lines = md_content.split('\n')
        in_table = False
        table_data = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            line_stripped = line.strip()
            
            # Tables
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
                # End of table
                if len(table_data) > 1:
                    table = Table(table_data, hAlign='LEFT')
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4472C4')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                        ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ]))
                    story.append(table)
                    story.append(Spacer(1, 0.2*inch))
                in_table = False
                table_data = []
            
            # Headings
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
            
            # Horizontal rule
            elif line_stripped == '---':
                story.append(Spacer(1, 0.15*inch))
            
            # Code blocks
            elif line_stripped.startswith('```'):
                code_lines = []
                i += 1
                while i < len(lines) and not lines[i].strip().startswith('```'):
                    code_lines.append(lines[i])
                    i += 1
                if code_lines:
                    code_text = '\n'.join(code_lines).strip()
                    story.append(Paragraph(code_text, code_style))
                    story.append(Spacer(1, 0.1*inch))
            
            # Blockquote
            elif line_stripped.startswith('> '):
                quote_text = line_stripped[2:].strip()
                p = Paragraph(quote_text, styles['Normal'])
                p_block = Paragraph(f"<i>{quote_text}</i>", ParagraphStyle('Quote', parent=styles['Normal'], leftIndent=30, textColor=colors.HexColor('#666666')))
                story.append(p_block)
                story.append(Spacer(1, 0.08*inch))
            
            # Bullet lists
            elif line_stripped.startswith('- '):
                bullet_text = line_stripped[2:].strip()
                story.append(Paragraph(f"• {bullet_text}", ParagraphStyle('Bullet', parent=styles['Normal'], leftIndent=20)))
            
            # Numbered lists
            elif re.match(r'^\d+\.\s', line_stripped):
                match = re.match(r'^(\d+)\.\s(.*)', line_stripped)
                if match:
                    num_text = match.group(2).strip()
                    num = match.group(1)
                    story.append(Paragraph(f"{num}. {num_text}", ParagraphStyle('Numbered', parent=styles['Normal'], leftIndent=20)))
            
            # Regular paragraph
            elif line_stripped:
                story.append(Paragraph(line_stripped, styles['Normal']))
            else:
                story.append(Spacer(1, 0.05*inch))
            
            i += 1
        
        doc.build(story)
        print(f"✓ Created {output_file}")
    
    if __name__ == '__main__':
        if len(sys.argv) < 2:
            print("Usage: python export_participant_guides_pdf.py phase1-participants.md [phase2-participants.md] [phase3-participants.md]")
            sys.exit(1)
        
        for input_file in sys.argv[1:]:
            if not Path(input_file).exists():
                print(f"Error: {input_file} not found")
                continue
            md_to_pdf(input_file)

except ImportError as e:
    print(f"Error: Required library not found: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
