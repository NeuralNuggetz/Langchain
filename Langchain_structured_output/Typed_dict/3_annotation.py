from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI(model= "gpt-5-nano-2025-08-07")


#schema
class Review(TypedDict):
    summary:Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[str, "Return sentiment of the review, positive, negative or neutral."]

structed_model = model.with_structured_output(Review)


result = structed_model.invoke("""
             The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
             """)

print(result)
print(result['summary'])
print(result['sentiment'])

# We didnt write in prompt to find summary and sentiment but how schema send predefined prompt at backend
'''
You ara an AI assistant that extracts structured insights from text. Given a product review extract:
- Summaray : A brief overview of the main points,  
-Sentiment:Overall  tone of the review (positive, negative, neutral). Return the response in JSON format.
'''