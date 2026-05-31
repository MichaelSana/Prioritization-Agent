from datetime import datetime, timezone
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class CalendarConnector:

    @staticmethod
    def get_calendar_service():
        creds = None

        if os.path.exists('credentials/calendar_token.json'):
            creds = Credentials.from_authorized_user_file(
                'credentials/calendar_token.json',
                SCOPES
            )

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/calendar_credentials.json',
                    SCOPES
                )

                creds = flow.run_local_server(port=0)

            with open('credentials/calendar_token.json', 'w') as token:
                token.write(creds.to_json())

        return build('calendar', 'v3', credentials=creds)

    async def fetch_events(self, max_results=20):
        """
        Fetch upcoming calendar events.
        """

        service = self.get_calendar_service()

        now = datetime.now(timezone.utc).isoformat()

        results = (
            service.events()
            .list(
                calendarId='primary',
                timeMin=now,
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime'
            )
            .execute()
        )

        events = results.get('items', [])

        if not events:
            return []

        formatted_events = []

        for event in events:
            start = event.get('start', {})
            end = event.get('end', {})

            start_time = (
                start.get('dateTime')
                or start.get('date')
            )

            end_time = (
                end.get('dateTime')
                or end.get('date')
            )

            formatted_events.append({
                "id": event.get("id"),
                "title": event.get("summary", "Untitled Event"),
                "description": event.get("description", ""),
                "location": event.get("location", ""),
                "start_time": start_time,
                "end_time": end_time,
                "status": event.get("status"),
                "creator": event.get("creator", {}).get("email"),
                "organizer": event.get("organizer", {}).get("email"),
            })

        return formatted_events