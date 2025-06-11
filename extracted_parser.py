import os

def xml_parser(source_dir='extracted'):
    if not os.path.exists(source_dir):
        print("❌ Oh oh, looks like source destination does not exist")
        return
    
    for filename in os.listdir(source_dir):
        if filename.endswith('.xml'):
            xml_path = os.path.join(source_dir, filename)
            with open(xml_path, 'r') as f:
                print(f"📂 Reading: {filename}")
                # Later you'll use: xml.etree.ElementTree to parse this
