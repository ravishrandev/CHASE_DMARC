import os
import gzip
import zipfile

def extract_compressed_files(source_dir='downloads', dest_dir='extracted'):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Handle .gz files
        if filename.endswith('.gz'):
            xml_filename = filename.replace('.gz', '.xml')
            xml_path = os.path.join(dest_dir, xml_filename)

            print(f"🧩 Extracting GZ: {filename} -> {xml_filename}")

            with gzip.open(file_path, 'rb') as f_in:
                with open(xml_path, 'wb') as f_out:
                    f_out.write(f_in.read())

        # Handle .zip files
        elif filename.endswith('.zip'):
            print(f"🧩 Extracting ZIP: {filename}")
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(dest_dir)  # Extracts all files to dest_dir

    print("✅ All .gz and .zip files extracted.")
