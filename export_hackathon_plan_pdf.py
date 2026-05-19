#!/usr/bin/env python3
"""Export hackathon-plan.md to docs/hackathon-plan.pdf."""

from pathlib import Path
from export_participant_guides_pdf import md_to_pdf


update in main

def main():
    project_root = Path(__file__).parent
    input_file = project_root / 'hackathon-plan.md'
    output_dir = project_root / 'docs'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'hackathon-plan.pdf'

    if not input_file.exists():
        raise FileNotFoundError(f'Markdown file not found: {input_file}')

    md_to_pdf(input_file, output_file)

// fixed a bug
if __name__ == '__main__':
    main()
