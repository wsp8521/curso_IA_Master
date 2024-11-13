import os
from langchain_openai import ChatOpenAI
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.utilities import PythonREPL #biblioteca que executa código python


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

python_repl = PythonREPL()

#transformando código python em uma tool
python_tool = Tool(
    name='Python tool', #nome da tool
    #descrição que é uma instrução será entendida pelo agent ia
    description='um shell Python. Use isso para executar códigos python. Executar apenas código pyton válidos' 
                'se você precisar obter o retorno do código, use a função "print(...)." ',
    func=python_repl.run
    
)

#criando agente
agente = create_python_agent(
    llm = modelo,
    tool=python_tool,
    verbose=True #exeibi sequencia lógia que o agente utilizou para montar a resposta
)


prompt_template = PromptTemplate(
    input_variables=['query'],
    template=''' resolva o seguinte problema: {query}. Responda tudo em português brasileiro.'''
)

pergunta=r'quanto é 20% de 3000'
prompt = prompt_template.format(query=pergunta)
response = agente.invoke(prompt)
print(response.get('output'))

