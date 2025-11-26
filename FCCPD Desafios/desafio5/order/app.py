from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/orders")
def get_orders():
    return jsonify([
        {"id": 101, "user_id": 1, "total": 250.50},
        {"id": 102, "user_id": 2, "total": 120.00}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
