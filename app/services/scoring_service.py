from datetime import datetime


class ScoringService:

    def calculate_priority(
        self,
        urgency: float,
        importance: float,
        stakeholder_weight: float,
        effort: float
    ) -> float:

        return (
            urgency * 0.4 +
            importance * 0.3 +
            stakeholder_weight * 0.2 -
            effort * 0.1
        )

    def deadline_score(self, deadline):

        if not deadline:
            return 0.2

        delta = deadline - datetime.utcnow()

        hours = delta.total_seconds() / 3600

        if hours < 4:
            return 1.0

        if hours < 24:
            return 0.8

        return 0.5