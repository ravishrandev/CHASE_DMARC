from gmail_service import get_gmail_service
from dmarc_downloader import download_dmarc_reports
from dmarc_extractor import extract_gz_files
from extracted_parser import parse_dmarc_reports
from print_dmarc import print_dmarc_table

if __name__ == '__main__':
    print("🚀 Starting DMARC report downloader...")
    service = get_gmail_service()
    download_dmarc_reports(service)
    extract_gz_files()
    records = parse_dmarc_reports()
    print_dmarc_table(records)

