from pdf2docx import Converter

def convert_pdf_to_doc(pdf_path, doc_path):
    # Create a PDF to DOCX converter object
    cv = Converter(pdf_path)

    # Convert the PDF file to DOCX format
    cv.convert(doc_path, start=0, end=None)

    # Close the converter
    cv.close()

# Example usage
convert_pdf_to_doc( 'pdfconverter/pdfs/Group12_Bird_Drone.pdf' , 'pdfconverter/output.docx')
