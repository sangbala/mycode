from flask import Flask
from flask import redirect

app = Flask (__name__)

@app.route("/one")
def one():
    return "Hello World!"

@app.route("/two/<adjective>")
def two(adjective):
    return f"I hope today is (adjective)!"

@app.route("/three", methods=["PUT","DELETE"])
def three():
    return "Changes and deletions only,please"

@app.route("/four")
def fourth():
    return redirect("one")

