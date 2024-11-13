import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')
loader = TextLoader('base_conhecimento.txt')
#document = loader.load() #lendo documento e armazenando na variavel


print(loader.load()