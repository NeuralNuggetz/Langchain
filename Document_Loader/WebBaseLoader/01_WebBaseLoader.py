from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = 'gpt-5-nano')

prompt = PromptTemplate(
    template = 'Answer the following question \n {question} from the following text - \n {text}',
    input_variables = ['question', 'text']
)

parser = StrOutputParser()

url = 'https://www.91mobiles.com/apple-mdh84hn-a-m5-16-gb-1-tb-mac-laptop-price-in-india-173891'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'What is the price of the laptop?', 'text':docs[0].page_content})

print(result)
