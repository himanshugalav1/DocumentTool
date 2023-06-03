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

# Usage example
doc_to_pdf('pdfconverter/doc/CY101-Manual Physical Chemistry_version2 (1) (1).doc', 'output1.pdf')
