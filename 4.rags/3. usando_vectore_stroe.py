import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain #classe que traz chains pre-definidos
from langchain.chains.retrieval import create_retrieval_chain



os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
modelo = ChatOpenAI(model='gpt-3.5-turbo')
persist_direcotry= 'db' #criando diretorio de base de dados 
embedding = OpenAIEmbeddings()

#buscando informações na base de dados
vectore_store = Chroma(
    persist_directory=persist_direcotry,
    embedding_function=embedding,
    collection_name='manual_notebook' #nome atribuido á coleção
)

#transformando dados em um retiver e que sera passado par a ia
retriver = vectore_store.as_retriever()

system_prompt = '''
    use o contexto para responder as perguntas.
    Contexto:{context}
'''

prompt = ChatPromptTemplate(
    [
        ('system',system_prompt ),
        ('human', '{input}'),
    ]
)


chains = create_stuff_documents_chain(
    llm=modelo,
    prompt=prompt
)

chains_retreaver = create_retrieval_chain(
    retriever=retriver,
    combine_docs_chain=chains
)

pergunta = "Qual a marca do notebook"

response = chains_retreaver.invoke(
    {'input':pergunta},
)

print(response['answer'])
