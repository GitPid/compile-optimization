

from langchain_openai import ChatOpenAI

# 配置 DeepSeek 模型
llm = ChatOpenAI(
    model="deepseek-chat",  # 模型名称固定
    base_url="https://api.deepseek.com/v1",  # 官方接口地址
    temperature=0.5,
)

# 测试调用
response = llm.invoke("你好，请介绍一下自己")
print(response.content)

test
hot test

