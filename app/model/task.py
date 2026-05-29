from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class UnifiedTask:
    id: str
    source: str
    title: str
    description: str
    priority_score: float
    deadline: datetime | None
    estimated_effort_hours: int
    stakeholders: List[str]
    tags: List[str]