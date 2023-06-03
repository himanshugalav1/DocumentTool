# DOCX to PDF converter
from docx2pdf import convert
def docx_to_pdf(input_file, output_file):
    convert(input_file, output_file)

# Notice that the output filename need not be
# the same as the docx

def docx_bulk_conversion(folder_name):
    convert(folder_name)
    
# Usage example 
docx_to_pdf('pdfconverter/docx/Group12_Bird_Drone.docx', 'pdfconverter/pdfs/Mine1.pdf')
# Usage example 
# docx_bulk_conversion('pdfconverter/docx')
