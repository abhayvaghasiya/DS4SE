import os
import subprocess

# Base directory where zip folders are located
base_dir = '/Users/abhayvaghasiya/Desktop/DS4SE/java_parser'

# Directory to extract contents of each zip folder
extract_dir = '/Users/abhayvaghasiya/Desktop/DS4SE/java_parser'

# Iterate over each zip file in the base directory
for zip_file in os.listdir(base_dir):
    if zip_file.endswith('.zip'):
        # Construct full path to the zip file
        zip_path = os.path.join(base_dir, zip_file)
        # Directory to extract this particular zip
        current_extract_dir = os.path.join(extract_dir, zip_file[:-4])  # removes .zip
        os.makedirs(current_extract_dir, exist_ok=True)
        
        # Unzip the file
        subprocess.run(['unzip', '-o', zip_path, '-d', current_extract_dir])

        # Run JavaParser on each jar file in the extracted directory
        for file in os.listdir(current_extract_dir):
            if file.endswith('.jar'):
                jar_path = os.path.join(current_extract_dir, file)
                rsf_path = os.path.join(current_extract_dir, f"{file[:-4]}.rsf")
                fv_path = os.path.join(current_extract_dir, f"{file[:-4]}.fv")
                package_prefix = "org.apache.hadoop.hdfs"  # Change as per your need

                # Command to run JavaParser
                command = [
                    'java', '-jar', '/Users/abhayvaghasiya/Desktop/DS4SE/java_parser',
                    jar_path, rsf_path, fv_path, package_prefix
                ]
                subprocess.run(command)
