from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = 'gpt-5-nano', temperature = 0.7, max_completion_tokens=500)

result = model.invoke("what is the capital of india")

print(result.content)