import requests as rq
import os
from zipfile import ZipFile
from urllib.parse import urlparse

# Script for downloading the dataset from the web, and extracting it to the data folder
dl_urls = [
    "https://www.kaggle.com/datasets/yashusinghal/electric-vehicle-population-dataset/download?datasetVersionNumber=1"
]

def download_file(url):
    # Sends a GET request to the provided URL
    response = rq.get(url)
    # If the response status code is 200 (HTTP OK), return the content of the response
    if response.status_code == 200:
        return response.content
    else:
        # If the response status code is not 200, print an error message and return None
        print(f"Failed to download {url}")
        return None
    
def extract_zip(z_content, path):
    # Open the zip file
    with ZipFile(z_content) as z_file:
        # Extract all files from the zip file to the specified path
        z_file.extractall(path)

def main():
    # Define the name of the folder where the files will be saved
    folder = "data"
    # If the folder does not exist, create it
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # For each URL in the list of URLs
    for url in dl_urls:
        # Parse the URL to get the path
        parsed = urlparse(url)
        # Get the filename from the path
        filename = os.path.basename(parsed.path)
        
        # Download the file from the URL
        file_content = download_file(url)
        # If the file was successfully downloaded
        if file_content:
            # Define the path where the file will be saved
            file_path = os.path.join(folder, filename)
            # Open the file in write-binary mode and write the content to it
            with open(file_path, 'wb') as f:
                f.write(file_content)
            
            # If the file is a zip file
            if file_path.endswith(".zip"):
                # Extract the zip file
                extract_zip(file_path)
                # Remove the original zip file
                os.remove(file_path)
                
# If this script is run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()