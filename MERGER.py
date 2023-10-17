from PyPDF2 import PdfMerger
import os

pdfs = [
    r'Statement\Statements of Accounts - Michael Brennan - 15.10.2023.pdf',
    r'Statement\A315 Water Edge 9.pdf',
    r'Statement\A401 Water Edge 7.pdf'
]

# Create a PdfMerger instance
merger = PdfMerger()

for pdf in pdfs:
    if os.path.exists(pdf):  # Check if the file exists
        merger.append(pdf)
    else:
        print(f"Warning: File '{pdf}' not found. Skipped.")

merger.write('Statements of Accounts - Michael Brennan - 15.10.2023.pdf')
merger.close()