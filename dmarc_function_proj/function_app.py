import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 0 22 * * 0", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def weeklyDmarcSummary(myTimer: func.TimerRequest) -> None:
    import os
    from gmail_service import get_gmail_service
    from dmarc_downloader import download_dmarc_reports
    from dmarc_extractor import extract_compressed_files
    from extracted_parser import parse_dmarc_reports
    from html_formatter import generate_html_table

    logging.info("🚀 Starting DMARC report downloader...")
    service = get_gmail_service()
    download_dmarc_reports(service)
    extract_compressed_files()
    records = parse_dmarc_reports()
    html_output = generate_html_table(records)
    
    output_dir = "html"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "weekly_dmarc_summary.html")
    with open(output_path, "w") as f:
        f.write(html_output)
    logging.info(f"HTML report saved as {output_path}")