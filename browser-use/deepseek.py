import asyncio
import os

from browser_use import Agent
from browser_use.llm import ChatDeepSeek
from browser_use.browser import BrowserProfile

# Add your custom instructions
extend_system_message = """
Remember the most important rules: 
1. When performing a search task, open https://www.google.com/ first for search. 
2. Final output.
"""
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
if deepseek_api_key is None:
	print('Make sure you have DEEPSEEK_API_KEY:')
	print('export DEEPSEEK_API_KEY=your_key')
	exit(0)

profile = BrowserProfile(
    keep_alive=True
)


async def main():
	llm = ChatDeepSeek(
		base_url='https://api.deepseek.com/v1',
		model='deepseek-chat',
		api_key=deepseek_api_key,
	)

	agent = Agent(
		task='navigate to bilibili.com and search for "DeepSeek AI"',
		llm=llm,
		use_vision=False,
		message_context=extend_system_message,
		browser_profile=profile
	)
	await agent.run()


asyncio.run(main())