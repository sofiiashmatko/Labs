from flask import Flask, request, jsonify
import json
import base64
from functools import wraps

app = Flask(__name__)

USERS_FILE = "users.txt"
ITEMS_FILE = "items.json"


# ---------- BASIC AUTH ----------
def check_auth(username, password):
    with open(USERS_FILE, "r") as f:
        for line in f:
            user, pwd = line.strip().split(":")
            if user == username and pwd == password:
                return True
    return False


def authenticate():
    resp = jsonify({"message": "Authentication required"})
    resp.status_code = 401
    resp.headers["WWW-Authenticate"] = 'Basic realm="Login Required"'
    return resp


def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth:
            return authenticate()
        try:
            scheme, encoded = auth.split()
            username, password = base64.b64decode(encoded).decode().split(":")
        except Exception:
            return authenticate()
        if not check_auth(username, password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


# ---------- FILE OPS ----------
def load_items():
    try:
        with open(ITEMS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


def save_items(items):
    with open(ITEMS_FILE, "w") as f:
        json.dump(items, f, indent=4)


# ---------- SIMPLE INDEX ----------
@app.route("/")
def index():
    return "Catalog service is running. Use /items endpoint."


# ---------- /items ----------
@app.route("/items", methods=["GET", "POST"])
@require_auth
def items():
    items = load_items()

    if request.method == "GET":
        return jsonify(items)

    if request.method == "POST":
        new_item = request.json
        items.append(new_item)
        save_items(items)
        return jsonify({"message": "Item added", "item": new_item}), 201


# ---------- /items/<id> ----------
@app.route("/items/<item_id>", methods=["GET", "PUT", "DELETE"])
@require_auth
def item_by_id(item_id):
    items = load_items()
    item = next((i for i in items if str(i.get("id")) == str(item_id)), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    if request.method == "GET":
        return jsonify(item)

    if request.method == "PUT":
        updated_data = request.json
        item.update(updated_data)
        save_items(items)
        return jsonify({"message": "Item updated", "item": item})

    if request.method == "DELETE":
        items.remove(item)
        save_items(items)
        return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
