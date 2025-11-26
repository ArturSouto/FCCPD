from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Alice", "activeSince": "2022-01-10"},
        {"id": 2, "name": "Bruno", "activeSince": "2023-03-15"},
        {"id": 3, "name": "Carlos", "activeSince": "2024-05-01"},
        {"id": 4, "name": "Daniela", "activeSince": "2021-11-22"},
        {"id": 5, "name": "Eduardo", "activeSince": "2020-07-08"},
        {"id": 6, "name": "Fernanda", "activeSince": "2023-09-19"},
        {"id": 7, "name": "Gabriel", "activeSince": "2022-06-30"}
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
