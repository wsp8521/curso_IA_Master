import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate # classe que permite a criação de templates de conversa
from langchain.prompts import HumanMessagePromptTemplate #classe usada para criar templates de mensagens que representam as interações de um usuário humano
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

#criando um template de conversa para ser utilizado por um modelo
chat_template = ChatPromptTemplate.from_messages(
    [
    SystemMessage(content='Você deve responder baseado nos dados geograficos a região do Brasil'), #passando a diretriz para o modelo
    HumanMessagePromptTemplate.from_template("Fale sobre a região {regiao}"), 
    AIMessage(content="Claro, iremos coletar os dados da região solicitada "), #mensagem o modelo
    HumanMessage(content="Certifique-se de informar a culinária da região"),
    AIMessage(content="Claro. aqui estão dos dados solicitados"),
    ]
)

prompt = chat_template.format_messages(regiao='Norte')
response = modelo.invoke(prompt)
print(response.content)