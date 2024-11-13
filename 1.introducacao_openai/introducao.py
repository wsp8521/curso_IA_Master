from dotenv import load_dotenv
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('TOKEN_OPENIA'))

response = client.chat.completions.create(
    model="gpt-3.5-turbo", #modelo
    messages=[{
        #especifica o papel de quem está enviando a mensagem. os valores são:
        #user - Representa a mensagem enviada pelo usuário.
        #assistant - Refere-se às respostas geradas pelo próprio modelo de IA (ou assistente).
        #system - Usado para definir regras e instruções sobre o comportamento do assistente durante a interação.
        
        "role": "system", "content": "calcule prazo processual de acordo com os prazos do  Código de Processo Civil (CPC). Mostre apenas a data final. \
            não explique o que são os prazos" ,
        "role":"user", "content": "prazo final de Embargos de declaração a partit de 16/10/2024?  Mostre apenas a data final."
               }],

    stream=True,
    temperature=0.5
  
)

# Exibir a resposta
#print(response.choices[0].message.content)


#usar o codigo se stream=True,
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

