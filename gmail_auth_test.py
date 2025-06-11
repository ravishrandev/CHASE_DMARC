from __future__ import print_function                           #compatibility with < python 3
import os.path                                                  #check if token exist
from google.auth.transport.requests import Request              #handle refreshing tokens securely
from google.oauth2.credentials import Credentials               #store and load Gmail access tokens
from google_auth_oauthlib.flow import InstalledAppFlow          #initiate Oauth browser popup 
from googleapiclient.discovery import build                     #create service objec to talk to Gmail API

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None

    # Load credentials from token.json if it exists
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid credentials, prompt login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Connect to Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # List the 5 latest messages in the inbox
    results = service.users().messages().list(userId='me', maxResults=10, q='subject:report has:attachment').execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
    else:
        print("Latest messages:")
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = msg_data['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            print("-", subject)

if __name__ == '__main__':
    print("🚀 Script started")

    main()
