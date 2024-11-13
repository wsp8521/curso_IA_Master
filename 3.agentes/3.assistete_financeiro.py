import os
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.utilities import PythonREPL #biblioteca que executa código python


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

prompt='''
        você pe um assistente financeiro que responderá as perguntas dando dicas financeiras e de investimentos.
        Responda tudo em português.
        Pergunta: {q}
        
'''

prompt_template = PromptTemplate.from_template(prompt)

#CRIANDO TOOLS
python_repl = PythonREPL()

#criando tool que executa código python
python_tool = Tool(
    name='Python tool', #nome da tool
    #descrição que é uma instrução será entendida pelo agent ia
    description='um shell Python. Use isso para executar códigos python. Executar apenas código pyton válidos' 
                'se você precisar obter o retorno do código, use a função "print(...)." ',
    func=python_repl.run
    
)

#criando tool que faz busca na internte
search = DuckDuckGoSearchRun()

docuk_duck=Tool(
    name='Busca DuckDuck',
    description=''' Encontre na internet informações sobre economia e opções de investimentos.
                    Você deve buscar na internet as melhores dicas de investimentos usando esta ferramenta.
                    Responda diretamente. sua resposta deve informar que ha elementos na internet ''',
    func=search.run
)

react_instruction = hub.pull('hwchase17/react') #baixando prompt prontos no hub langchain

tools = [python_tool,docuk_duck]#criand lista de tools

#criando agentes
agente = create_react_agent(
    llm = modelo,
    tools=tools,
    prompt=react_instruction,
)

#criando executor do agente
agente_executor = AgentExecutor(
    agent=agente,
    tools=tools,
    verbose=True
)

question = '''
    Recebo 2000 reais por meis e gastos 3 mil. Me de dicas de como melhorar minha situação financeira e ainda sobrar dinheiro pra investir.
'''

response = agente_executor.invoke(
    input={'input':prompt_template.format(q=question)}
)

print(response.get('output'))