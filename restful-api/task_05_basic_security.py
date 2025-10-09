#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "my_secret_key_1"
jwt = JWTManager(app)


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
# To run it -> curl -u user1:password http://localhost:5000/basic-protected
@auth.login_required # protects only users can access 
def basic_protected():
    return "Basic Auth: Access Granted\n"

@app.route("/login", methods=["POST"])
# To run it, choose user1/admin1 -> curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "admin1", "password": "password"}'
def login():
    # get the data from the user in json and convert it into a python dict 
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username==verify_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid username or password"}), 401
 
@app.route('/jwt-protected', methods=["GET"])
# To run it -> curl -X GET "http://localhost:5000/jwt-protected" -H "Authorization: Bearer TokenHere"
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted\n"

@app.route('/admin-only', methods=["GET"])
# To run it -> curl -X GET "http://localhost:5000/admin-only" -H "Authorization: Bearer TokenHere"
@jwt_required()
def admi_only():
    check_user = get_jwt_identity()

    if check_user not in users or users[check_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted\n"

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)