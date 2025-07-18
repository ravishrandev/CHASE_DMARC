from google.auth.transport.requests import Request                   #handle refreshing tokens securely
from google.oauth2.credentials import Credentials                 #store and load Gmail access tokens
from google_auth_oauthlib.flow import InstalledAppFlow            #initiate Oauth browser popup 
from googleapiclient.discovery import build                      #create service objec to talk to Gmail API
import os                                                       #use for directory purposes

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)
