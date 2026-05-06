from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding =  OpenAIEmbeddings(model = 'text-embedding-3-small', dimensions=300)

documents = ["Virat Kohli is an Indian Known for his aggressive batting and leadership.",
             "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
             "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
             "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."]

query = "tell me about bumrah"

doc_embeddings =  embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1])[-1]
print(index, float(score)) 

print(query)
print(documents[index])
print("Similarity Score:", similarity_scores[index])