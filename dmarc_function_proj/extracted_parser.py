import os
import xml.etree.ElementTree as ET

def parse_dmarc_reports(source_dir='extracted'):
    records = []  # Store each record as a dict

    if not os.path.exists(source_dir):
        print("❌ Oh oh, looks like source destination does not exist")
        return records

    for filename in os.listdir(source_dir):
        if filename.endswith('.xml'):
            xml_path = os.path.join(source_dir, filename)
            print(f"📂 Reading: {filename}")
            tree = ET.parse(xml_path)
            root = tree.getroot()

            for record in root.findall('record'):
                row = record.find('row')
                policy = row.find('policy_evaluated')
                identifiers = record.find('identifiers')
                auth_results = record.find('auth_results')

                # Defensive lookups to avoid NoneType errors
                dkim = auth_results.find('dkim') if auth_results is not None else None
                spf = auth_results.find('spf') if auth_results is not None else None

                records.append({
                    'ip': row.findtext('source_ip', default='N/A'),
                    'count': row.findtext('count', default='0'),
                    'envelope_to': identifiers.findtext('envelope_to', default='N/A'),
                    'envelope_from': identifiers.findtext('envelope_from', default='N/A'),
                    'header_from': identifiers.findtext('header_from', default='N/A'),
                    'dkim_domain': dkim.findtext('domain', default='N/A') if dkim is not None else 'N/A',
                    'dkim_result': dkim.findtext('result', default='N/A') if dkim is not None else 'N/A',
                    'spf_result': spf.findtext('result', default='N/A') if spf is not None else 'N/A',
                    'disposition': policy.findtext('disposition', default='N/A'),
                })

    return records
