import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate # classe que permite a criação de templates de conversa
from langchain_core.output_parsers import StrOutputParser #classe que  garante que a saída seja adequadamente tratada como uma string


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

prompt_pergunta = (
    PromptTemplate.from_template( 
    '''
        Classifique a pergunta do usuário em um dos seguintes setores:
         - Financeiro
         - Suporte técnico
         - outras informações
         
         Pergunta: {pergunta}
    
    '''
    )
    | modelo
    | StrOutputParser()
)

#rota financeiro
prompt_financeiro = (
    PromptTemplate.from_template(
        '''
            Você é um especialista financeiro. 
            Sempre responda às perguntas começando com um "Bem-vindo ao Setor Financeiro"
            Responda à pergunta do usuário:
            Pergunta: {pergunta}
        '''
    )
    | modelo
    | StrOutputParser()
)

#rota suporte técnico
prompt_suporte_tecnico = (
    PromptTemplate.from_template(
        '''
            Você é um especialista em suporte técnico. 
            Sempre responda às perguntas começando com um "Bem-vindo ao Setor de Suporte Técnico"
            Responda à pergunta do usuário:
            Pergunta: {pergunta}
        '''
    )
    | modelo
    | StrOutputParser()
)

#rota outro setor
prompt_outro_setor = (
    PromptTemplate.from_template(
        '''
            Você é um especialista em informações gerais. 
            Sempre responda às perguntas começando com um "Bem-vindo a Central de informações
            Responda à pergunta do usuário:
            Pergunta: {pergunta}
        '''
    )
    | modelo
    | StrOutputParser()
)


def routers(topic):
    topic = topic.lower()
    if 'financeiro' in topic:
        return prompt_financeiro
    elif 'técnico' in topic:
        return prompt_suporte_tecnico
    else:
        return prompt_outro_setor
    

pergunta = input("Qual a sua pergunta: ")

classificacao = prompt_pergunta.invoke({'pergunta':pergunta})
response_setor = routers(topic=classificacao)
response = response_setor.invoke({'pergunta':pergunta})
print(response)

