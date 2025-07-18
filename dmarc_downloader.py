import base64
import os
from datetime import datetime, timedelta

today = datetime.now()

#get the days range for downloading files
def get_week_range():
    
    #Get monday (Weekday 0)
    monday = today- timedelta(days=today.weekday())
    #Get next monday (start of next week)
    next_monday = monday + timedelta(days=7)

    #Format as YYYY/MM/DD (Gmail expects this)
    return monday.strftime('%Y/%m/%d'), next_monday.strftime('%Y/%m/%d')


#finds mime payload structure.
def find_attachments(payload):
    """Recursively find all parts with filename and attachmentId."""
    attachments = []            #empty list to store attachments

    if 'parts' in payload:
        for part in payload['parts']:
            attachments.extend(find_attachments(part))
    else:
        filename = payload.get('filename')
        body = payload.get('body', {})
        attachment_id = body.get('attachmentId')

        if filename and attachment_id:
            attachments.append({
                'filename': filename,
                'attachmentId': attachment_id
            })

    return attachments

def download_dmarc_reports(service, max_results=30, save_dir="downloads"):
    os.makedirs(save_dir, exist_ok=True)

    monday_str, next_monday_str = get_week_range()

    results = service.users().messages().list(
        userId='me',
        maxResults=max_results,
        q = f'subject:"Report domain" has:attachment after:{monday_str} before:{next_monday_str}'
    ).execute()

    messages = results.get('messages', [])
    print("📊 Estimated total matches:", results.get('resultSizeEstimate'))
    print("📥 Returned message count:", len(messages))
    print("Reports between date:", monday_str,"and", today)

    if not messages:
        print("No messages found.")
        return

    print("📂 Downloading DMARC Reports...")
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        print("-", subject)

        attachments = find_attachments(msg_data['payload'])

        if not attachments:
            print("⚠️ No downloadable attachments found.")
            continue

        for att in attachments:
            attachment = service.users().messages().attachments().get(
                userId='me',
                messageId=msg['id'],
                id=att['attachmentId']
            ).execute()

            file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
            file_path = os.path.join(save_dir, att['filename'])

            with open(file_path, 'wb') as f:
                f.write(file_data)
            print("✅ Saved:", file_path)
