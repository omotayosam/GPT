import tarfile
import os
from tqdm import tqdm

# Directory containing the .tar files
tar_directory = "/Users/ayo/Downloads/openwebtext"

# Directory where you want to extract the files
extract_path = "/Users/ayo/Downloads/openwebtextxtrct"

# Get a list of all files in the directory
all_files = os.listdir(tar_directory)

# Filter only .tar files
tar_files = [file for file in all_files if file.endswith(".tar")]

# Loop through each .tar file
for tar_file in tar_files:
    # Open the .tar file
    with tarfile.open(os.path.join(tar_directory, tar_file), 'r') as tar:
        # Extract all contents into the specified directory with tqdm progress bar
        with tqdm(total=len(tar.getnames()), desc=f"Extracting {tar_file}", unit="file") as pbar:
            for member in tar.getmembers():
                tar.extract(member, path=extract_path)
                pbar.update(1)
