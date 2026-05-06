from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model  = ChatOpenAI(model = 'gpt-5-nano-2025-08-07', temperature = 0.7, max_completion_tokens=500)

messages = [
    SystemMessage(content='You are a helpful AI assistant'),
    HumanMessage(content='tell me about langchain'),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)