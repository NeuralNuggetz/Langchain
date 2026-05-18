from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = 'gpt-5-nano')

prompt = PromptTemplate(
    template = 'Write a summary for the following poem - \n {poem}',
    input_variables = ['poem']
)

parser = StrOutputParser()
loader = TextLoader('Document_Loader/Text_Loader/cricket.txt', encoding='utf-8')
docs = loader.load()
print(docs[0])

print(docs[0].metadata)
print(docs[0].page_content)


chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})

print(result)