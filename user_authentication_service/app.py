#!/usr/bin/env python3
""" Basic flask app module"""


from auth import Auth
from flask import Flask, jsonify, request
app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def basic():
    """ Basic app route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """End-point to register a user"""
    try:
        user = AUTH.register_user(request.form["email"],
                                  request.form["password"])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
