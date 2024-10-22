import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate # classe que permite a criação de templates de conversa
from langchain.prompts import HumanMessagePromptTemplate #classe usada para criar templates de mensagens que representam as interações de um usuário humano
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI('gpt-3.5-turbo')


