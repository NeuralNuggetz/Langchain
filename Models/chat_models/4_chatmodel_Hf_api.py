from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",  # small + works on Groq
    task="text-generation",
    provider="novita",
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of india")
print(result.content)