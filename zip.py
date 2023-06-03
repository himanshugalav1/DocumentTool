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

import zipfile

def unzip_file(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Example usage
unzip_file('pdfconverter/out.zip', 'pdfconverter/hehe')

# Example usage
zip_folder('pdfconverter/doc', 'pdfconverter/out.zip')
