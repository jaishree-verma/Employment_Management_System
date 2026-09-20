# Clean Black and White Printable Stylesheet for Easy Student Revision

CSS_STYLES = """
@page {
    size: A4 portrait;
    margin: 20mm 18mm 20mm 18mm;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: Arial, Helvetica, sans-serif;
        font-size: 9pt;
        color: #444444;
    }
    @top-right {
        content: "Employment Management System | Quick Revision Guide";
        font-family: Arial, Helvetica, sans-serif;
        font-size: 8.5pt;
        color: #555555;
    }
}

@page:first {
    margin: 25mm 20mm 25mm 20mm;
    @bottom-center { content: ""; }
    @top-right { content: ""; }
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, Helvetica, 'Segoe UI', sans-serif;
    color: #111111;
    background-color: #ffffff;
    line-height: 1.6;
    font-size: 10pt;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: #000000;
    font-family: Arial, Helvetica, sans-serif;
    page-break-after: avoid;
}

h1.section-title {
    font-size: 14pt;
    border-bottom: 1.5px solid #000000;
    padding-bottom: 4px;
    margin-top: 22px;
    margin-bottom: 10px;
}

.section-number {
    font-weight: bold;
    margin-right: 6px;
}

h2 {
    font-size: 12pt;
    margin-top: 14px;
    margin-bottom: 6px;
    border-left: 3px solid #000000;
    padding-left: 6px;
}

h3 {
    font-size: 10.5pt;
    margin-top: 10px;
    margin-bottom: 4px;
}

p {
    margin-bottom: 8px;
    color: #222222;
    text-align: left;
}

ul, ol {
    margin-top: 4px;
    margin-bottom: 10px;
    padding-left: 22px;
}

li {
    margin-bottom: 4px;
    color: #222222;
}

/* Page Break Utilities */
.page-break {
    page-break-before: always;
    break-before: page;
}

.avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* Cover Page - Clean Black & White Academic Style */
.cover-page {
    border: 2px solid #000000;
    padding: 30px 25px;
    min-height: 240mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #ffffff;
    page-break-after: always;
}

.cover-header {
    text-align: center;
    border-bottom: 2px solid #000000;
    padding-bottom: 25px;
}

.cover-title {
    font-size: 26pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.cover-subtitle {
    font-size: 13pt;
    color: #333333;
    font-style: italic;
    margin-bottom: 15px;
}

.cover-badge {
    display: inline-block;
    border: 1px solid #000000;
    padding: 4px 12px;
    font-size: 9pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.cover-metadata {
    margin: 30px 0;
}

.cover-meta-table {
    width: 100%;
    border-collapse: collapse;
    margin: 0 auto;
}

.cover-meta-table td {
    padding: 8px 12px;
    border: 1px solid #333333;
    font-size: 9.5pt;
}

.cover-meta-table td.label {
    width: 35%;
    font-weight: bold;
    background-color: #f2f2f2;
}

.cover-footer {
    border-top: 1px solid #000000;
    padding-top: 15px;
    text-align: center;
    font-size: 9pt;
    color: #444444;
}

/* Status Badges - Black & White */
.badge {
    display: inline-block;
    padding: 1px 6px;
    border: 1px solid #000000;
    font-size: 7.5pt;
    font-weight: bold;
    text-transform: uppercase;
    background: #ffffff;
}

.badge-implemented {
    background: #000000;
    color: #ffffff;
}

.badge-partial {
    background: #eeeeee;
    color: #000000;
    border: 1px solid #666666;
}

.badge-planned, .badge-future {
    background: #ffffff;
    color: #000000;
    border: 1px dashed #444444;
}

.badge-not-implemented {
    background: #ffffff;
    color: #777777;
    border: 1px solid #cccccc;
}

/* Tables - Clean, Standard Black & White */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 12px;
    font-size: 9pt;
    page-break-inside: auto;
}

tr {
    page-break-inside: avoid;
}

th {
    background: #f0f0f0;
    color: #000000;
    font-weight: bold;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #333333;
    font-size: 8.5pt;
}

td {
    padding: 6px 8px;
    border: 1px solid #666666;
    vertical-align: top;
    color: #111111;
}

tr:nth-child(even) td {
    background-color: #fafafa;
}

/* Clean Callout Boxes - Black & White */
.box-note {
    border: 1px solid #000000;
    border-left: 4px solid #000000;
    background-color: #f9f9f9;
    padding: 8px 12px;
    margin: 8px 0;
    font-size: 9pt;
    page-break-inside: avoid;
}

.box-title {
    font-weight: bold;
    margin-bottom: 3px;
    text-transform: uppercase;
    font-size: 8.5pt;
}

/* Code Blocks */
pre {
    background: #f5f5f5;
    color: #000000;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 8px 10px;
    margin: 6px 0 10px 0;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8pt;
    line-height: 1.4;
    page-break-inside: avoid;
    overflow-x: auto;
}

code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    background: #eeeeee;
    color: #000000;
    padding: 1px 4px;
    border: 1px solid #dddddd;
    border-radius: 3px;
}

pre code {
    background: transparent;
    padding: 0;
    border: none;
}

/* Flowchart and Diagram Containers - B&W */
.diagram-box {
    border: 1px solid #333333;
    padding: 10px;
    margin: 10px 0;
    text-align: center;
    background: #ffffff;
    page-break-inside: avoid;
}

.diagram-caption {
    font-size: 8.5pt;
    font-weight: bold;
    margin-bottom: 6px;
    text-transform: uppercase;
}

/* 2-Column Layout */
.row-2 {
    display: flex;
    gap: 12px;
    margin-bottom: 8px;
}

.col-2 {
    flex: 1;
    border: 1px solid #cccccc;
    padding: 8px 10px;
    background: #ffffff;
}
"""
