from flask import Flask, request, jsonify, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "waitlist.json"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/article")
def article():
    return render_template("article.html")



@app.route("/join-waitlist", methods=["POST"])
def join_waitlist():
    data = request.json

    user_entry = {
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email"),
        "timestamp": datetime.utcnow().isoformat()
    }

    # Create file if not exists
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

    # Append data
    with open(DATA_FILE, "r+") as f:
        users = json.load(f)
        users.append(user_entry)
        f.seek(0)
        json.dump(users, f, indent=4)

    return jsonify({"status": "success", "message": "User added to waitlist"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
