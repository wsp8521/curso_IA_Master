import os
from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate #classe que permite a construção de templates dinamicos

os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')

modelo = OpenAI()

templates = '''
 traduza o texto do {indioma1} para o {indioma2}:
 {texto}
'''

prompt_templates = PromptTemplate.from_template(template=templates) # permite criar um prompt de maneira simplificada a partir de uma string de template fornecida
prompt = prompt_templates.format( #método preenche os campos (placeholders) definidos no template com os valores passados como argumentos.
    indioma1 = "português",
    indioma2 = "inglês",
    texto = "Bom dia"
)

response = modelo.invoke(prompt)

print(response)
