import os
import sys
import subprocess
import time

from doc_builder.styles import CSS_STYLES
from doc_builder.part1 import get_part1_html
from doc_builder.part2 import get_part2_html
from doc_builder.part3 import get_part3_html
from doc_builder.part4 import get_part4_html
from doc_builder.part5 import get_part5_html

def build_html():
    print("[1/4] Assembling HTML Document for Employment Management System...")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employment Management System - Technical Documentation</title>
    <style>
{CSS_STYLES}
    </style>
</head>
<body>
{get_part1_html()}
{get_part2_html()}
{get_part3_html()}
{get_part4_html()}
{get_part5_html()}
</body>
</html>
"""
    output_html_path = os.path.abspath("Employment_Management_System_Technical_Documentation.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[2/4] HTML Document written to: {output_html_path} ({len(html)} bytes)")
    return output_html_path

def render_pdf(html_path):
    print("[3/4] Rendering PDF via Headless Microsoft Edge Engine...")
    pdf_path = os.path.abspath("Employment_Management_System_Technical_Documentation.pdf")
    
    # Locate msedge
    msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(msedge_path):
        msedge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if not os.path.exists(msedge_path):
            raise FileNotFoundError("Neither Microsoft Edge nor Google Chrome could be found.")

    file_url = f"file:///{html_path.replace(os.sep, '/')}"
    
    cmd = [
        msedge_path,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        "--no-pdf-header-footer",
        file_url
    ]
    
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"[4/4] Successfully generated PDF: {pdf_path} ({size_kb:.2f} KB)")
        return pdf_path
    else:
        raise RuntimeError("PDF file was not created by the browser engine.")

def verify_pdf(pdf_path):
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        print("=" * 60)
        print(f"PDF AUDIT SUCCESSFUL!")
        print(f"File: {os.path.basename(pdf_path)}")
        print(f"Total Pages Generated: {len(reader.pages)}")
        print(f"File Size: {os.path.getsize(pdf_path) / 1024:.2f} KB")
        print("=" * 60)
    except Exception as e:
        print(f"Warning during PDF validation: {e}")

if __name__ == "__main__":
    html_file = build_html()
    pdf_file = render_pdf(html_file)
    verify_pdf(pdf_file)
