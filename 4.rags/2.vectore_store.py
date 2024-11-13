import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter #importando classe que divide texto em chunks

os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')

files = './4.rags/laptop_manual.pdf'

loader_docs = PyPDFLoader(files).load() #lendo arquivo

text_spliters = RecursiveCharacterTextSplitter( #definindo as configurações do chunks
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks = text_spliters.split_documents( #dividindo o documento em chuks
    documents=loader_docs
)

persist_direcotry= 'db' #criando diretorio de base de dados 

#criando um banco de vetor 
embedding = OpenAIEmbeddings()
vector_store = Chroma.from_documents(
    documents = chunks ,
    embedding=embedding,
    persist_directory=persist_direcotry, #persistindo dados no crhoma
    collection_name='manual_notebook'
)

# retriaver = vector_store.as_retriever()

# prompt = hub.pull('rlm/rag-prompt')

# # criando chain
# rag_chain = (
#     {
#        'context':retriaver,
#        'question':RunnablePassthrough(),
#     }
#     |prompt
#     |modelo
#     |StrOutputParser()
# )

# try:
#     while True:
#         question = input("Qual a sua dúvida: ")   
#         response = rag_chain.invoke(question)
#         print(response)
#         print()
        
# except KeyboardInterrupt:
#     exit()