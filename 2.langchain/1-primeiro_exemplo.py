import os
from langchain_openai import OpenAI, ChatOpenAI


os.environ['OPENAI_API_KEY']=os.getenv('TOKEN_OPENIA')
#utilização do ivoke
model = OpenAI()
response = model.invoke(
    input ='Quem descobriu o Brasil?',
    temperature = 0.1,
    max_tokens = 200
)

#utilização do chat
chat = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.5,
    max_tokens=200,
     
)

messages=[
    {"role": "system", "content": "você é um historiador. Dê respostas curtas"},
    {"role":"user", "content": "Quem descobriu o Brasil"} 
    ]

print(model.invoke(messages))

        