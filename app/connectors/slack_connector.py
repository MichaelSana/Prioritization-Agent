class SlackConnector:

    async def fetch_messages(self):

        return [
            {
                "id": "slack_1",
                "channel": "engineering",
                "message": "Production issue impacting customers",
            }
        ]