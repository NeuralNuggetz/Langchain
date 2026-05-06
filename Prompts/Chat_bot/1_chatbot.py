from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = 'gpt-5-nano-2025-08-07', temperature = 0.7, max_completion_tokens=1000)

chat_history = [
    SystemMessage(content = 'You are a helpful AI assistant')
]



while True:
    user_input = input('you:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('bot:', result.content)
print(chat_history)