from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a Linkedin post about {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI(model = 'gpt-5-nano')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(
        prompt1, model, parser
    ),
    'linkedin': RunnableSequence(
        prompt2, model, parser
    )}
)

result = parallel_chain.invoke({'topic':'AI'})

print(result)