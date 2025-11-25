import time
import requests

url = "http://server:8080"

while True:
    try:
        print("Realizando requisição...")
        resposta = requests.get(url)
        print("Resposta:", resposta.text)
    except Exception as e:
        print("Erro ao conectar:", e)

    time.sleep(3)
