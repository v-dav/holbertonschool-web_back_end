#!/usr/bin/env python3
""" Basic flask app module"""


from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET"])
def basic():
    """ Basic app route"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
