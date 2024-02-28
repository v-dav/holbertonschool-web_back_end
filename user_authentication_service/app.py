#!/usr/bin/env python3
""" Basic flask app module"""


from auth import Auth
from flask import abort, Flask, jsonify, request
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """A login route for the app
    """
    user_email = request.form["email"]
    user_pwd = request.form["password"]
    if AUTH.valid_login(user_email, user_pwd):
        session_id = AUTH.create_session(user_email)
        json_response = jsonify({"email": user_email, "message": "logged in"})
        json_response.set_cookie("session_id", session_id)
        return json_response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
