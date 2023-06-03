from PyPDF2 import PdfMerger

def combine_pdfs(file1, file2, output_file):
    merger = PdfMerger()
    merger.append(file1)
    merger.append(file2)
    merger.write(output_file)
    merger.close()

# Usage example
combine_pdfs('whatsapp/10th.pdf', 'whatsapp/12th Hall Ticket.pdf', 'combined.pdf')

