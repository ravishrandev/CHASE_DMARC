import base64
import os

def download_dmarc_reports(service, max_results=10, save_dir="downloads"):
    os.makedirs(save_dir, exist_ok=True)

    results = service.users().messages().list(
        userId='me',
        maxResults=max_results,
        q='subject:report has:attachment'
    ).execute()

    messages = results.get('messages', [])
    if not messages:
        print("No messages found.")
        return

    print("Latest DMARC Reports:")
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        parts = msg_data['payload'].get('parts', [])
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        print("-", subject)

        for part in parts:
            filename = part.get('filename')
            if filename:
                attachment_id = part['body']['attachmentId']
                attachment = service.users().messages().attachments().get(
                    userId='me', messageId=msg['id'], id=attachment_id).execute()
                data = attachment['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                file_path = os.path.join(save_dir, filename)
                with open(file_path, 'wb') as f:
                    f.write(file_data)
                print("✅ Saved:", file_path)
