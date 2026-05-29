# from fastapi import FastAPI
# from app.api.routes import router

# app = FastAPI(
#     title="AI Priority Agent",
#     version="1.0.0"
# )

# app.include_router(router)

import asyncio
from connectors.gmail_connector import GmailConnector


async def main():
    connector = GmailConnector()

    emails = await connector.fetch_emails()

    for email in emails:
        print(email)


asyncio.run(main())