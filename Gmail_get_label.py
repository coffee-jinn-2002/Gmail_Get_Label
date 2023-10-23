import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# NOTE: Make sure to keep your SCOPES and other sensitive information private!
SCOPES = ['YOUR_SCOPE_HERE']

def gmail_authenticate():
    """Shows basic usage of the Gmail API.
    List the user's Gmail labels.
    """
    creds = None

    # Add your own mechanism to load credentials
    # e.g., from environment variables, configuration files, etc.
    # Ensure that credentials handling is secure.

    return build('gmail', 'v1', credentials=creds)

def list_labels(service):
    """
    List all labels in the user's mailbox.
    """
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'], label['id'])

def main():
    service = gmail_authenticate()
    list_labels(service)

if __name__ == '__main__':
    main()
