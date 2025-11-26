from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def get_users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bruno"},
        {"id": 3, "name": "Carlos"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
