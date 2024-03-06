#!/usr/bin/env python3
"""The basic app module"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """The welcome page"""
    return render_template("0-index.html")
