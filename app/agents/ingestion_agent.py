from app.agents.base import BaseAgent
from app.connectors.gmail_connector import GmailConnector
from app.connectors.slack_connector import SlackConnector


class IngestionAgent(BaseAgent):

    def __init__(self):
        self.gmail = GmailConnector()
        self.slack = SlackConnector()

    async def run(self, payload=None):

        emails = await self.gmail.fetch_emails()
        slack_messages = await self.slack.fetch_messages()

        unified_events = []

        unified_events.extend(emails)
        unified_events.extend(slack_messages)

        return unified_events