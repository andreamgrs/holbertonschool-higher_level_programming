#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

# Simulate users database
#users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, 
#         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    users_list = list(users.keys())
    return (users_list)

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_users_usernames(username):
    user_surname = users.get(username)
    if user_surname:
        return jsonify(user_surname)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"]) # Create new user with POST
def get_request():
    # get data JSON
    data_json = request.get_json()
    if not data_json or "username" not in data_json:
        return jsonify({"error": "Username is required"}), 400

    username = data_json["username"] # get username from data_json that looks like {key: value}
    users[username] = data_json # save all data_json by the key "username"

    return jsonify({
        "message": "User added",
        "user": data_json
    }), 201


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True) # Active debug mode, starts server at localhost:5000
