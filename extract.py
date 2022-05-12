import pdfplumber

# a single page
with pdfplumber.open(r'test.pdf') as pdf:
    first_page = pdf.pages[-0]
    print(first_page.extract_text())
