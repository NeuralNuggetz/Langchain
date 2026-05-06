from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional

load_dotenv()

model = ChatOpenAI(model= "gpt-5-nano-2025-08-07")


#schema
class Review(TypedDict):
    key_themes:Annotated[list[str],"write down all the key themes discussed in the review in a list"]
    summary:Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[str, "Return sentiment of the review, positive, negative or neutral."]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    Cons: Annotated[Optional[list[str]], "Write down all the Cons inside a list"]

structed_model = model.with_structured_output(Review)


result = structed_model.invoke("""
             I recently upgraded to the Samsung Galaxy s24 Ultra , and I must say, It's an absolute powerhouse! The Sanpdragon 8 Gen 3 processor makes everthing lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
                               
            The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200 MP camera-the night model is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
            However, the weight and size make it bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
                               
            Pros:
                Tnsanely powerful processor (great for gaming and productivity)
                Stunning 200MP camera with incredible zoom capabilities
                Long battery life with fast charging
                S-Pen support is unique and useful
            Cons:
                Bulky and heavy-not great for one-handed use
                Bloatware still exists in One UI
                Expensive compared to competitors
             """)

print(result)
print(result['summary'])
print(result['sentiment'])

# Output of the code
'''
{'key_themes': ['High-end performance and gaming capability', 'Stellar camera system with 200 MP sensor and strong zoom', 'Long battery life with fast charging', 'S-Pen integration for note-taking and sketches', 'Bulk/ergonomics and One UI bloatware', 'Premium price'], 'summary': 'The Galaxy S24 Ultra delivers top-tier speed, a standout 200 MP camera with impressive night performance and up to 100x zoom, plus solid all-day battery life and fast charging. S-Pen support adds practical productivity features. However, its bulk makes one-handed use awkward, One UI still carries noticeable bloatware, and the price remains steep for a flagship.', 'sentiment': 'Positive', 'pros': ['Extremely powerful processor (great for gaming and productivity)', 'Stunning 200 MP camera with strong night mode and impressive zoom', 'Long battery life with 45W fast charging', 'S-Pen integration adds handy note-taking and sketching capabilities'], 'Cons': ['Bulky and heavy—not ideal for one-handed use', 'Bloatware persists in Samsung One UI', 'Expensive compared to competitors']}
The Galaxy S24 Ultra delivers top-tier speed, a standout 200 MP camera with impressive night performance and up to 100x zoom, plus solid all-day battery life and fast charging. S-Pen support adds practical productivity features. However, its bulk makes one-handed use awkward, One UI still carries noticeable bloatware, and the price remains steep for a flagship.
Positive
'''