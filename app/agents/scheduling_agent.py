from app.agents.base import BaseAgent


class SchedulingAgent(BaseAgent):

    async def run(self, prioritized_tasks):

        ranked = prioritized_tasks["ranked_tasks"]

        schedule = []

        current_hour = 9

        for task in ranked:

            schedule.append({
                "task": task["id"],
                "start_hour": current_hour,
                "end_hour": current_hour + 1
            })

            current_hour += 1

        prioritized_tasks["schedule"] = schedule

        return prioritized_tasks