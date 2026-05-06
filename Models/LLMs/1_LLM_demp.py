from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-5-nano')
result = llm.invoke("Who is the president of India?")

print(result)