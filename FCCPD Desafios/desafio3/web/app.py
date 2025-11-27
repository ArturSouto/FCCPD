from flask import Flask
import redis
import mysql.connector
import os

app = Flask(__name__)

cache = redis.Redis(host=os.getenv("CACHE_HOST"), port=6379)

@app.route("/")
def index():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = connection.cursor()
    cursor.execute("SELECT 'Funcionando'")
    result = cursor.fetchone()

    cache.incr("visitas")
    visitas = cache.get("visitas").decode()

    return f"""
    <p>{result[0]}</p>
    <p>Visitas registradas no Redis: {visitas}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
