import os
import zipfile

# Function to extract zip files in the folder
def extract_zip_files(source_folder, destination_folder):
    # Get list of all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file is a zip file
        if filename.endswith('.zip'):
            file_path = os.path.join(source_folder, filename)
            print(f'Extracting {filename}...')
            try:
                # Open the zip file
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    # Extract all the contents into the destination folder
                    zip_ref.extractall(destination_folder)
                    print(f'{filename} extracted successfully!')
            except Exception as e:
                print(f'Failed to extract {filename}: {e}')

# Source folder containing zip files
source_folder = r'G:\edulyst ventures\minecraft-server\zips'  # Change this to your folder containing zip files
# Destination folder where zip files will be extracted
destination_folder = r'G:\edulyst ventures\minecraft-server\plugin'

# Call the function to extract zip files
extract_zip_files(source_folder, destination_folder)
