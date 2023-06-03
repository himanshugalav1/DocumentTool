import os
import subprocess

def unrar_file(rar_path, output_dir):
    # Get the full path to the unrar executable
    unrar_executable = "C:\Program Files\WinRAR\UnRAR"  # Replace with the actual path to the unrar executable

    # Check if the unrar executable exists
    if not os.path.isfile(unrar_executable):
        print(f"Unrar executable not found at: {unrar_executable}")
        return

    # Create the command to extract the RAR file
    command = [unrar_executable, 'x', '-y', rar_path, output_dir]

    # Run the command
    subprocess.run(command)

# Example usage
rar_file_path = 'pdfconverter/rar/Exp_7_G1.rar'
output_directory = 'pdfconverter/rar'

unrar_file(rar_file_path, output_directory)

# "C:\Program Files\WinRAR\UnRAR.exe"