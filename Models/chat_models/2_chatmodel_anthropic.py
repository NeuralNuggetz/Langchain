from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model_name= 'claude-2', timeout='', stop='')

'''
timeout -> If AI doesn't reply within X seconds, stop waiting and show an error
stop -> Imagine you ask someone to read a book aloud, but you say:

"Stop reading when you reach the word 'Chapter 2'"

That's exactly what stop does — it tells the AI:

"Stop generating text when you see this word/symbol"
'''


result = model.invoke("what is the capital of india")

print(result.content)
