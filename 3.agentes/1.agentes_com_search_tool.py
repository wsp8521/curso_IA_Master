import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.agents.agent_toolkits import create_python_agent


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

#definindo tool
wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(lang='pt')
)

#criando agente
agente = create_python_agent(
    llm = modelo,
    tool=wikipedia,
    verbose=True #exeibi sequencia lógia que o agente utilizou para montar a resposta
)

prompt_template = PromptTemplate(
    input_variables=['pesquisa'],
    template='''
        Pesquise na web sobre {pesquisa} e depois forneça um resumo sobre o assunto.
        Responda tudo em português brasileiro.
    
    '''
)

pergunta="Quem descobrio o brasil"

prompt = prompt_template.format(pesquisa=pergunta)

response = agente.invoke(prompt)

print(response.get('output'))