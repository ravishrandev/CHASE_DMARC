from gmail_service import get_gmail_service
from dmarc_downloader import download_dmarc_reports
from dmarc_extractor import extract_compressed_files
from extracted_parser import parse_dmarc_reports
#from print_dmarc import print_dmarc_table
from html_formatter import generate_html_table

if __name__ == '__main__':
    print("🚀 Starting DMARC report downloader...")
    service = get_gmail_service()
    download_dmarc_reports(service)
    extract_compressed_files()
    records = parse_dmarc_reports()
    html_output = generate_html_table(records)
    
    with open("weekly_dmarc_summary.html", "w") as f:
        f.write(html_output)
    print("✅ HTML report saved as weekly_dmarc_summary.html")

