from app.agents.base import BaseAgent
from app.services.embedding_service import EmbeddingService


class ContextAgent(BaseAgent):

    def __init__(self):
        self.embedding_service = EmbeddingService()

    async def run(self, events):

        enriched = []

        for event in events:

            text = str(event)

            embedding = await self.embedding_service.create_embedding(text)

            event["embedding"] = embedding

            enriched.append(event)

        return enriched