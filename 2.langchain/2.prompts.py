import os
from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.cache import InMemoryCache #ferramenta que armazena em memória os resultados de chamadas anteriores de funções ou consultas em fluxos de linguagem. 
from langchain_community.cache import SQLiteCache # ferramenta que Armazena no banco de dados sqlite as respostas geradas por modelos de linguagem
from langchain.globals import set_llm_cache # utilizada para definir o cache que será usado para armazenar as respostas geradas por modelos de linguagem (LLMs)

os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')

modelo = OpenAI()

set_llm_cache(SQLiteCache(database_path='openai_cache.db')) #criando base de dados para armazenar a resposta do medelo

prompt = "Fale sobre o presidente Lula"

print(f'RESPOSTA 1: {modelo.invoke(prompt)} ')
print(f'RESPOSTA 2: {modelo.invoke(prompt)} ')