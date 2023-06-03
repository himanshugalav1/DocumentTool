from pptx import Presentation

def convert_ppt_to_pdf(input_file, output_file):
    presentation = Presentation(input_file)
    presentation.save(output_file)

# Usage example
convert_ppt_to_pdf('pdfconverter/ppt/The Circuit Breakers.pptx', 'output.pdf')
