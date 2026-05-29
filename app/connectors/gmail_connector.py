import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Read-only Gmail access
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GmailConnector:

    @staticmethod
    def get_gmail_service():
        creds = None

        # Authenticate if needed
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/gmail_credentials.json',
                    SCOPES
                )
                creds = flow.run_local_server(port=0)

            # Save token
            with open('credentials/token.json', 'w') as token:
                token.write(creds.to_json())

        return build('gmail', 'v1', credentials=creds)

    async def fetch_emails(self, max_results=5):
        """
        Fetch recent Gmail messages.
        """

        service = self.get_gmail_service()

        results = (
            service.users()
            .messages()
            .list(userId='me', maxResults=max_results)
            .execute()
        )

        messages = results.get('messages', [])

        if not messages:
            return []

        emails = []

        for msg in messages:
            message = (
                service.users()
                .messages()
                .get(userId='me', id=msg['id'])
                .execute()
            )

            payload = message.get('payload', {})
            headers = payload.get('headers', [])

            subject = next(
                (
                    header['value']
                    for header in headers
                    if header['name'] == 'Subject'
                ),
                'No Subject'
            )

            sender = next(
                (
                    header['value']
                    for header in headers
                    if header['name'] == 'From'
                ),
                'Unknown Sender'
            )

            snippet = message.get('snippet', '')

            emails.append({
                "id": msg['id'],
                "subject": subject,
                "sender": sender,
                "body": snippet,
            })

        return emails