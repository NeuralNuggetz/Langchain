from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate 1 interesting facts about {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI(model = 'gpt-5-nano', temperature = 0.7, max_completion_tokens=1000)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'India'})

print(result)

chain.get_graph().print_ascii()