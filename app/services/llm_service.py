from openai import OpenAI

client = OpenAI()


class LLMService:

    async def prioritize(self, tasks):

        prompt = f"""
        You are an executive prioritization AI.

        Analyze these tasks and rank them.

        Tasks:
        {tasks}
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You prioritize work intelligently."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content