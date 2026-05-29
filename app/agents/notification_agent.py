from app.agents.base import BaseAgent


class NotificationAgent(BaseAgent):

    async def run(self, payload):

        print("Sending daily summary...")

        print(payload["llm_summary"])

        return True