from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()

model = ChatOpenAI(model = 'gpt-5-nano-2025-08-07', temperature = 0.7)

st.header('Research Tool')

# Dynamic Prompt
paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention IS All You Need",
                                                           "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                                                            "GPT-3: Language Models are Few-Shot Learners", "Difussion Models Best GANs on Image Synthesis" ])

style_input = st.selectbox("Select Explanation Style",[
    "Begineer-Friendly",
    "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select Explanation Length",
                            ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", 
                             "Long (6+ paragraphs)"])


# First Method to use Prompt Template
'''
template = PromptTemplate(
    template="""
        Please summarize the research paper titled "{paper_input}" with the following specifications:
        Explanation Style: {style_input}
        Explanation Length: {length_input}
        1. Mathematical Details:
            - Include relevant mathematical equations if present in the paper.
            - Explain the mathematical concepts using simple, intutive code snippets where applicable.
        2. Analogies:
            -Use relatable analogies to simplify complex ideas.
        If certain information is not available in the paper,
        respond with : "Insufficient information available" Instead of guessing.
        Ensure the summary is clear, accurate and alligned with the provide style and length.
        """,

input_variables=["paper_input", "style_input", "length_input"],

# validate_template -> to check if all placeholders are filled. if any placeholders missing (length_input is not mention in input_variables) or added extra  then show error.
validate_template=True
) 
'''

# Second Method to use Prompt template (Prompt outside code)
template = load_prompt('template.json')



'''
# Double time invoke method
# fill the placeholders
prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})


if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)

'''

# Single time invoke method
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)