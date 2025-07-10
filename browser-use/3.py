from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from pydantic import SecretStr

# Add your custom instructions
extend_system_message = """
记住最重要的规则:
1、执行搜索任务时，优先打开 https://www.bing.com/?mkt=zh-CN 进行搜索。
2、最后的输出结果，要用中文回答用户的问题。
"""
api_key = os.getenv('DEEPSEEK_API_KEY')


async def main():
    # Initialize the model
    llm = ChatOpenAI(base_url='https://api.deepseek.com/v1', model='deepseek-chat', api_key=SecretStr(api_key))
    agent = Agent(
        task="近期发布的《提振消费专项行动方案》，有哪些值得关注的内容？",
        llm=llm,
        use_vision=False,
        message_context=extend_system_message
    )
    await agent.run()


asyncio.run(main())