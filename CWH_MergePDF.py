import PyPDF2
import os

def merge(pdfs, output):
    pdfMerger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        pdfMerger.append(pdf)

    with open(output, 'wb') as f:
        pdfMerger.write(f)

files = []
output = 'combined_all.pdf'

os.chdir('../temp')
print(f"changed directory: {os.getcwd()}")

for file in os.listdir('../temp'):
    if file.endswith('.pdf'):
        files.append(file)

print(files)
merge(files, output)
