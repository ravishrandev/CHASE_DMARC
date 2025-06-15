import os
import xml.etree.ElementTree as ET

def xml_parser(source_dir='extracted'):
    if not os.path.exists(source_dir):
        print("❌ Oh oh, looks like source destination does not exist")
        return
    
    for filename in os.listdir(source_dir):                     #go through all files in the folder
        if filename.endswith('.xml'):                          
            xml_path = os.path.join(source_dir, filename)       #create file path for future use
            with open(xml_path, 'r') as f:
                print(f"📂 Reading: {filename}")
                tree = ET.parse(xml_path)
                root = tree.getroot() 
                #print(ET.tostring(root, encoding='unicode'))
                for record in root.findall('record'):
                    row = record.find('row')
                    source_ip = row.find('source_ip').text
                    count = row.find('count').text

                    print("📌 Source IP:", source_ip)
                    print("📊 Count:", count)