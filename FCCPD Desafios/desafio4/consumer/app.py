from flask import Flask
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://user:5001/users"

@app.get("/combined")
def combined():
    try:
        response = requests.get(USER_SERVICE_URL)
        users = response.json()

        result = []
        for user in users:
            result.append(f"Usuario {user['name']} desde {user['activeSince']}\n")

        return "\n".join(result)

    except Exception as e:
        return f"Erro ao acessar o serviço de usuários: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
