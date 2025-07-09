import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatOpenAI
import os
api_key = os.getenv('DEEPSEEK_API_KEY')
print(api_key)

extend_system_message = """
response in json format!
"""

async def main():
    llm = ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=api_key)
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        #llm=ChatOpenAI(model="o4-mini", temperature=1.0),
        llm=llm,
        message_context=extend_system_message
    )
    await agent.run()

asyncio.run(main())