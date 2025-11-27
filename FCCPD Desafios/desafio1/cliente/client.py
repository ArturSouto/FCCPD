import time
import requests

SERVER_URL = "http://server:8080"

print("Cliente iniciado...", flush=True)

while True:
    try:
        print("------", flush=True)
        print("Requisitando servidor...", flush=True)
        response = requests.get(SERVER_URL, timeout=5)
        print("Resposta:", response.text, flush=True)
    except Exception as e:
        print("Erro ao acessar o servidor:", e, flush=True)
    
    time.sleep(3)
