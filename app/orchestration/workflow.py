from app.agents.ingestion_agent import IngestionAgent
from app.agents.context_agent import ContextAgent
from app.agents.prioritization_agent import PrioritizationAgent
from app.agents.scheduling_agent import SchedulingAgent
from app.agents.notification_agent import NotificationAgent


class AgentWorkflow:

    def __init__(self):

        self.ingestion_agent = IngestionAgent()
        self.context_agent = ContextAgent()
        self.prioritization_agent = PrioritizationAgent()
        self.scheduling_agent = SchedulingAgent()
        self.notification_agent = NotificationAgent()

    async def execute(self):

        raw_events = await self.ingestion_agent.run()

        contextualized = await self.context_agent.run(raw_events)

        prioritized = await self.prioritization_agent.run(contextualized)

        scheduled = await self.scheduling_agent.run(prioritized)

        await self.notification_agent.run(scheduled)

        return scheduled