import os
import xml.etree.ElementTree as ET

def parse_dmarc_reports(source_dir='extracted'):

    records = []                                                #store records in dictionary

    if not os.path.exists(source_dir):
        print("❌ Oh oh, looks like source destination does not exist")
        return records
    
    for filename in os.listdir(source_dir):                     #go through all files in the folder
        if filename.endswith('.xml'):                          
            xml_path = os.path.join(source_dir, filename)       #create file path for future use
            print(f"📂 Reading: {filename}")
            tree = ET.parse(xml_path)
            root = tree.getroot() 
            #print(ET.tostring(root, encoding='unicode'))

            for record in root.findall('record'):
                row = record.find('row')
                policy = row.find('policy_evaluated')

                records.append({
                    'ip': row.find('source_ip').text,
                    'count': row.find('count').text,
                    'spf': policy.find('spf').text,
                    'dkim': policy.find('dkim').text,
                    'disposition' : policy.find('disposition').text
                })

    return records