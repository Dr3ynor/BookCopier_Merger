import PyPDF2

def merge_pdfs(input_pdfs, output_pdf):
    merger = PyPDF2.PdfMerger()

    try:
        for pdf in input_pdfs:
            merger.append(pdf)

        with open(output_pdf, 'wb') as merged_pdf:
            merger.write(merged_pdf)

        print(f'Merged PDFs successfully. Output saved to: {output_pdf}')

    except Exception as e:
        print(f'Error merging PDFs: {e}')

input_pdfs = [f"{i}.pdf" for i in range(691)]
print(input_pdfs)
output_pdf = 'merged_output.pdf'

merge_pdfs(input_pdfs, output_pdf)
