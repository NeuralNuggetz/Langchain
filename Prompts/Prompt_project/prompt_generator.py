from langchain_core.prompts import PromptTemplate

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

template.save('template.json')

'''
 LangChainDeprecationWarning: The method `BasePromptTemplate.save` was deprecated in langchain-core 1.2.21 and will be removed in 2.0.0. Use `Use `dumpd`/`dumps` from `langchain_core.load` to serialize prompts and `load`/`loads` to deserialize them.` instead.
template.save('template.json')
'''