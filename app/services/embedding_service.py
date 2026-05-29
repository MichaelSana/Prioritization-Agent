from openai import OpenAI

client = OpenAI()


class EmbeddingService:

    async def create_embedding(self, text: str):

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding