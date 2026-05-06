from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# text = "This is a test document."
# query_result = embedding.embed_query(text)
# print(str(query_result))



# documents

documents = ["Delhi is the capital of India", 
             "London is the capital of England", 
             "Paris is the capital of France"]

result = embedding.embed_documents(documents)

print(str(result))