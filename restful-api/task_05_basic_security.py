#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "my_secret_key_1"

# Simulate users database
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users[username]["password"], password): # .get[username] obtain the hash from that user, check_p_h compares passwords 
        return username

@app.route('/basic-protected', methods=["GET"])
@auth.login_required # protects only users can access 
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    # get the data from the user in json and convert it into a python dict 
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    get_user = users.get(username)

    if not get_user or not check_password_hash(get_user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401


    payload = {
        "username": get_user["username"],
        "role": get_user["role"],
    }

    token = jwt.encode(payload, app.config["JWT_SECRET_KEY"], algorithm="HS256")
    return jsonify({"access_token": token})
 
@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admi_only():
    check_user = get_jwt_identity()

    if check_user not in users or users[check_user]["role"] != "admi":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admi Access: Granted"

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)