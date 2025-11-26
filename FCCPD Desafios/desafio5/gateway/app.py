from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service:5001/users"
ORDER_SERVICE_URL = "http://order-service:5002/orders"


@app.get("/users")
def proxy_users():
    try:
        resp = requests.get(USER_SERVICE_URL, timeout=5)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.get("/orders")
def proxy_orders():
    try:
        resp = requests.get(ORDER_SERVICE_URL, timeout=5)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.get("/")
def home():
    return jsonify({"message": "Gateway funcionando"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
