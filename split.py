from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_file, output_directory):
    pdf_reader = PdfReader(input_file)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        
        output_file_path = f"{output_directory}/page_{page_num + 1}.pdf"
        with open(output_file_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Usage example
split_pdf('pdfconverter/pdfs/combined.pdf', 'pdfconverter/output_directory')
