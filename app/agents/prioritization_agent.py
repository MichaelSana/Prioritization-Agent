from app.agents.base import BaseAgent
from app.services.scoring_service import ScoringService
from app.services.llm_service import LLMService


class PrioritizationAgent(BaseAgent):

    def __init__(self):
        self.scoring = ScoringService()
        self.llm = LLMService()

    async def run(self, events):

        scored = []

        for event in events:

            score = self.scoring.calculate_priority(
                urgency=0.9,
                importance=0.8,
                stakeholder_weight=0.7,
                effort=0.4
            )

            event["priority_score"] = score

            scored.append(event)

        ranked = sorted(
            scored,
            key=lambda x: x["priority_score"],
            reverse=True
        )

        explanation = await self.llm.prioritize(ranked)

        return {
            "ranked_tasks": ranked,
            "llm_summary": explanation
        }