#############################################################################################################
# PDF Merger Code
from PyPDF2 import PdfMerger

def combine_pdfs(file1, file2, output_file):
    merger = PdfMerger()
    merger.append(file1)
    merger.append(file2)
    merger.write(output_file)
    merger.close()


#############################################################################################################
# PDF Spliter Code
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_file, output_directory):
    pdf_reader = PdfReader(input_file)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        
        output_file_path = f"{output_directory}/page_{page_num + 1}.pdf"
        with open(output_file_path, 'wb') as output_file:
            pdf_writer.write(output_file)

#############################################################################################################
# DOC to PDF converter
import os
import win32com.client as win32

def doc_to_pdf(input_file, output_file):
    # Create a COM object for Microsoft Word
    word = win32.Dispatch('Word.Application')
    word.Visible = False

    try:
        # Open the input DOC file
        doc = word.Documents.Open(os.path.abspath(input_file))

        # Save as PDF
        doc.SaveAs(os.path.abspath(output_file), FileFormat=17)  # 17 stands for PDF format
        doc.Close()
    except Exception as e:
        print(f"Conversion failed: {str(e)}")
    finally:
        # Quit Word application
        word.Quit()

#############################################################################################################
# DOCX to PDF converter
from docx2pdf import convert

def docx_to_pdf(input_file, output_file):
    convert(input_file, output_file)

def docx_bulk_conversion(folder_name):
    convert(folder_name)
    
#############################################################################################################
# Image ( jpg , jpeg , png ) to PDF Converter

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

def convert_folder_to_pdf(folder_path, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    elements = []
    image_files = get_image_files_from_folder(folder_path)

    for image_file in image_files:
        img = Image(image_file)
        img.drawHeight = 500  # Adjust the image height as desired
        img.drawWidth = 500   # Adjust the image width as desired
        elements.append(img)

    doc.build(elements)

def get_image_files_from_folder(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png']
    image_files = []

    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in image_extensions:
                image_files.append(os.path.join(folder_path, file))

    return image_files

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image

def convert_images_to_pdf(image_files, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    elements = []
    for image_file in image_files:
        img = Image(image_file)
        img.drawHeight = 500  # Adjust the image height as desired
        img.drawWidth = 500   # Adjust the image width as desired
        elements.append(img)

    doc.build(elements)

#############################################################################################################
# PDF To Docx converter

from pdf2docx import Converter

def convert_pdf_to_doc(pdf_path, doc_path):
    # Create a PDF to DOCX converter object
    cv = Converter(pdf_path)

    # Convert the PDF file to DOCX format
    cv.convert(doc_path, start=0, end=None)

    # Close the converter
    cv.close()


#############################################################################################################
# Zip a file 

import zipfile
import os

def zip_folder(folder_path, output_path):
    # Ensure that the output path includes the .zip extension
    if not output_path.endswith('.zip'):
        output_path += '.zip'

    # Create a zip file object for writing
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Iterate over all files and subdirectories in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Add the file to the zip archive, preserving the directory structure
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

# UnZip a file

def unzip_file(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


# Usage example
combine_pdfs('whatsapp/10th.pdf', 'whatsapp/12th Hall Ticket.pdf', 'combined.pdf')
# Usage example
split_pdf('pdfconverter/pdfs/combined.pdf', 'pdfconverter/output_directory')
# Usage example
doc_to_pdf('pdfconverter/doc/CY101-Manual Physical Chemistry_version2 (1) (1).doc', 'output1.pdf')
# Usage example 
docx_to_pdf('pdfconverter/docx/Group12_Bird_Drone.docx', 'pdfconverter/pdfs/Mine.pdf')
# Usage example 
docx_bulk_conversion('pdfconverter/docx')
# Usage example
image_files = ['pdfconverter/images/aadhar.jpg', 'pdfconverter/images/N.Kannan.jpeg', 'pdfconverter/images/shre2.png']
convert_images_to_pdf(image_files, 'pdfconverter/output1.pdf')
# Usage example
convert_folder_to_pdf('pdfconverter/images' , 'pdfconverter/output.pdf')
# Example usage
convert_pdf_to_doc( 'pdfconverter/pdfs/Group12_Bird_Drone.pdf' , 'pdfconverter/output.docx')
# Example usage
unzip_file('pdfconverter/out.zip', 'pdfconverter/hehe')
# Example usage
zip_folder('pdfconverter/doc', 'pdfconverter/out.zip')

