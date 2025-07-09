import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent

from browser_use.llm import ChatGoogle
from browser_use import Agent
from dotenv import load_dotenv

# Read GOOGLE_API_KEY into env
load_dotenv()


async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatGoogle(model='gemini-2.0-flash-exp')
    )
    await agent.run()

asyncio.run(main())