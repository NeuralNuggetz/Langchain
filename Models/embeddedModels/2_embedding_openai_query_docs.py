from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-small', dimensions=32)

documents = ["Delhi is the capital of India", 
             "London is the capital of England", 
             "Paris is the capital of France"]


result = embedding.embed_documents(documents)

print(str(result))



# for query
'''
 text = "This is a test document."
 query_result = embedding.embed_query(text)
 print(str(query_result))
'''
