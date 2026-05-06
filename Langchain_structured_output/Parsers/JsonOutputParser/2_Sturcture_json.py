# This is example code to show we dont control structure of LLM output in json format

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",  # small + works on Groq
    task="text-generation",
    provider="novita",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()


template = PromptTemplate(
    template= 'Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={"format_instruction": parser.get_format_instructions()}

)

# 1st method
# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# 2nd method to invoke using chain
chain = template | model | parser

final_result = chain.invoke({'topic':'black hole'})


print(final_result)

# output 

'''
{'black_holes': [{'name': 'M87*', 'description': 'One of the closest supermassive black holes to Earth, located at the center of the Milky Way galaxy.', 'diameter': '12 million kilometers', 'mass': '6.5 billion times the mass of the sun'}, {'name': 'Cygnus X-1', 'description': 'A binary black hole system located in the constellation Cygnus, known for its bright X-ray emissions.', 'diameter': '1.4 billion kilometers', 'mass': '20 times the mass of the sun'}, {'name': 'G2 star system', 'description': 'A binary star system located in the constellation Sagittarius, containing two stars with a red supergiant companion.', 'diameter': '50 kiloparsecs', 'mass': '10 times the mass of the sun'}, {'name': 'A0620-00', 'description': 'A black hole candidate located in the constellation Monoceros, discovered in 2016.', 'diameter': '3.6 million kilometers', 'mass': '18 times the mass of the sun'}]}
'''
