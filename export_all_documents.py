#!/usr/bin/env python3
"""Generate the full document set under the docs folder with one command."""

from pathlib import Path
import subprocess
import sys

""" Update 2 in main branch """

def run_step(description, command, project_root):
    print(f"\n==> {description}")
    result = subprocess.run(command, cwd=project_root)
    if result.returncode != 0:
        print(f"Failed: {description}")
        sys.exit(result.returncode)


def main():
    project_root = Path(__file__).parent
    python_executable = sys.executable

    markdown_guides = [
        'phase1-participants.md',
        'phase2-participants.md',
        'phase3-participants.md',
        'phase1-proctor.md',
        'phase2-proctor.md',
        'phase3-proctor.md',
    ]

    run_step(
        'Export workflow guide DOCX',
        [python_executable, 'export_workflow_guide_docx.py'],
        project_root,
    )
    run_step(
        'Export workflow guide PDF',
        [python_executable, 'export_workflow_guide_pdf.py'],
        project_root,
    )
    run_step(
        'Export phase guide DOCX files',
        [python_executable, 'export_markdown_to_docx.py', *markdown_guides],
        project_root,
    )
    run_step(
        'Export phase guide PDF files',
        [python_executable, 'export_participant_guides_pdf.py', *markdown_guides],
        project_root,
    )
    run_step(
        'Generate hackathon plan DOCX',
        [python_executable, 'generate_hackathon_plan_docx.py'],
        project_root,
    )
    run_step(
        'Export hackathon plan PDF',
        [python_executable, 'export_hackathon_plan_pdf.py'],
        project_root,
    )

    print('\nAll supported documents were generated in the docs folder.')


if __name__ == '__main__':
    main()
