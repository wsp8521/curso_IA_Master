import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')
#loader = TextLoader('langchain/base_conhecimento.txt')
loader = PyPDFLoader('2.langchain/base_conhecimento.pdf')
documents = loader.load() #lendo documento e armazenando na variavel

prompt_template = PromptTemplate(
    input_variables=['contexto', 'pergunta'], # define as variáveis que serão preenchidas no template
    template=''' use o seguinte contexto para responder à pergunta.
    responda apenas com base nas informações fornecidas.
    Não utilize informações externas ao contexto.
    Contexto:{contexto}
    Pergunta; {pergunta}
    '''
    
)

chain = prompt_template | modelo | StrOutputParser()
pergunta = input("Pergunta: ")

respose = chain.invoke(
{
   'contexto' : '\n'.join(doc.page_content for doc in documents), #pecorrendo as páginas dos documentos
   'pergunta': pergunta
}
)

print(respose)