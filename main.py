import sys
import time
import requests
import json
from properties import API_KEY
from properties import URL_MODELS
from properties import ID_MODEL
from properties import URL_CHAT

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: python main.py <message>")
    exit(1)
else:
    message = sys.argv[1]


''' para realizar requisição simples e receber texto sem envio de mensagem 
headers = {
    "Authorization": f"Bearer {API_KEY}"
}
'''

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

body_message = {
    "model": ID_MODEL,
    "messages": [{
        "role": "user",
        "content": f"{message}clear"
        }]
}

body_message = json.dumps(body_message)

#lendo modelos disponíveis
#req = requests.get(URL_MODELS, headers=headers)

req = requests.post(URL_CHAT, headers=headers, data=body_message)
res = req.json()

message = res['choices'][0]['message']['content']

print("\n----------------------------------------------------------------------\n")

for caractere in message:
    print(caractere, end='', flush=True)
    time.sleep(0.1)

#print(message)

print("\n\n----------------------------------------------------------------------\n")
