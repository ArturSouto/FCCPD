from flask import Flask
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="db",
        user="admin",
        password="admin",
        dbname="desafio2"
    )

@app.get("/carros")
def listar_carros():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome FROM carros;")
        dados = cur.fetchall()
        cur.close()
        conn.close()

        resultado = ""
        for carro in dados:
            resultado += f"Carro {carro[1]} \t(id={carro[0]})\n"

        return resultado

    except Exception as e:
        return f"Erro ao acessar o banco: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
