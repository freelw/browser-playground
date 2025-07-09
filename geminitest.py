from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# 替换为你的 Gemini API 密钥
# 可以通过设置环境变量 GOOGLE_API_KEY 来避免直接在代码中硬编码
import os
print(os.environ["GOOGLE_API_KEY"])

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

messages = [
    HumanMessage(
        content="请给我一个关于人工智能和未来的简短故事。"
    )
]

response = llm.invoke(messages)
print(response.content)