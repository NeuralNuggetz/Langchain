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

def load_document(file_path):
    loader = TextLoader(file_path, encoding='utf-8')
    docs = loader.load()
    return {'poem': docs[0].page_content}

document_loader = RunnableLambda(load_document)


chain = document_loader | prompt | model | parser

result = chain.invoke('Document_Loader/Text_Loader/cricket.txt')

print(result)