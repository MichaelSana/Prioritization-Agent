from app.agents.base import BaseAgent
from app.connectors.gmail_connector import GmailConnector


class IngestionAgent(BaseAgent):

    def __init__(self):
        self.gmail = GmailConnector()

    async def run(self, payload=None):

        emails = await self.gmail.fetch_emails()

        unified_events = []
        unified_events.extend(emails)

        return unified_events