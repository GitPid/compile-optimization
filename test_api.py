
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-chat",  # 模型名称固定
    base_url="https://api.deepseek.com/v1",  # 官方接口地址
    temperature=0.7,
    streaming=True,  # 1. 增加stream参数
)

# 2. 使用stream方法进行流式输出
response = llm.stream("你好，请介绍一下自己")

# 3. for循环输出每个chunk
for chunk in response:
    print(chunk.content, end="", flush=True)  # 不换行并立即刷新输出

