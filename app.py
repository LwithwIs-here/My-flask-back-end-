from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Demo users (asli project mein database use karo)
USERS = {
    "admin": "1234",
    "rahul": "pass123",
}


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if username == "":
        return jsonify(ok=False, message="Username daalna zaroori hai."), 400
    elif password == "":
        return jsonify(ok=False, message="Password daalna zaroori hai."), 400
    elif username not in USERS:
        return jsonify(ok=False, message="Ye username nahi mila."), 401
    elif USERS[username] != password:
        return jsonify(ok=False, message="Password galat hai."), 401
    else:
        return jsonify(ok=True, message="Namaste, " + username + "! Login ho gaya."), 200


if __name__ == "__main__":
    app.run(debug=True)
