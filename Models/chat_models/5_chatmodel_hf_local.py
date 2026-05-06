from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os


os.environ['HF_HOME'] =  'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
        model_id="meta-llama/Llama-3.2-1B-Instruct",
        task = "text-generation",
        provider="novita",
        pipeline_kwargs=dict(
            temperature = 0.5,
            max_new_tokens = 100
        )
        )

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of india")
print(result.content)