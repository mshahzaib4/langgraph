from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

os.environ['LANGCHAIN_PROJECT'] = 'SEQUENTIAL LLM APP'

prompt_1 = PromptTemplate(
    template = 'Genrate detailed report on {topic}',
    input_varibale = ['topic']
)

prompt_2 = PromptTemplate(
    template = 'Genrate 5 pointer sumary from the following text {text}',
    input_varibale = ['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

CONFIG = {
    'tags': ['LLM APP', 'EARN', 'DETAIL'],
    'metadata': ['model', 'CHATGPT']
}

result = chain.invoke({ "topic": "how to Eran 1 Million dollars with in 2 year" })
print(result)