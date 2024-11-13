import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate # classe que permite a criação de templates de conversa
from langchain_core.output_parsers import StrOutputParser #classe que  garante que a saída seja adequadamente tratada como uma string


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

prompt_template = PromptTemplate.from_template( #from_template() é usada para criar um modelo a partir de uma string com placeholders,
    'fale sobre o carro {carro}'
)

#primeira forma de criar um chain
chain1 = prompt_template | modelo | StrOutputParser() #criando encadeamento de chains

#segunda forma de criar um chain
chain2 = (
    PromptTemplate.from_template(
        'fale sobre o carro {carro}'
    ) 
    | modelo
    | StrOutputParser()
    
    
)


response = chain1.invoke({'carro':"hb20"})
response2 = chain2.invoke({'carro':'onix'})

print(response2)