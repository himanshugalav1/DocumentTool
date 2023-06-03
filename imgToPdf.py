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


# Usage example
folder_path = 'pdfconverter/images'
output_file = 'pdfconverter/output.pdf'
convert_folder_to_pdf(folder_path, output_file)

# Usage example
image_files = ['pdfconverter/images/aadhar.jpg', 'pdfconverter/images/N.Kannan.jpeg', 'pdfconverter/images/shre2.png']
convert_images_to_pdf(image_files, 'pdfconverter/output1.pdf')
