import os
import gzip

def extract_gz_files(source_dir='downloads', dest_dir='extracted'):
    if not os.path.exists(dest_dir):     #check if destination folder exists, creates one if it doesnt
        os.makedirs(dest_dir)

    for filename in os.listdir(source_dir):                     #os.listdir gives a list of all finenames in folder
        if filename.endswith('.gz'):                            #filter .gz files we need
            gz_path = os.path.join(source_dir, filename)        #create gz file path to read and write
            xml_filename = filename.replace('.gz', '.xml')
            xml_path = os.path.join(dest_dir, xml_filename)     #save converted file into dest folder - extracted that is

            print(f"🧩 Extracting {filename} -> {xml_filename}")

            #with automatically closes files so its safe
            with gzip.open(gz_path, 'rb') as f_in :             #open .gz file in binary read mode
                with open(xml_path, 'wb') as f_out:             #opens .gz file in binart write mode
                    f_out.write(f_in.read())                    #write raw content (compressed XML data) into new file

    print("✅ All .gz files extracted.")            
