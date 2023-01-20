#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import html
import requests

app = Flask(__name__)
CORRECT_ANSWER = ""


@app.route("/correct")
def correct():
    return render_template("correct.html")


@app.route("/incorrect")
def incorrect():
    return render_template("incorrect.html")


@app.route("/<username>")
def index(username):
    global CORRECT_ANSWER
    URL = "https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=multiple"
    data = requests.get(URL).json()
    json_data = data['results']
    question_dict = json_data[3]
    question = html.unescape(question_dict['question'])
    CORRECT_ANSWER = question_dict['correct_answer']
    answers = [question_dict['correct_answer']]
    answers.extend(question_dict['incorrect_answers'])

    options = {}
    opts = []
    for i in range(4):
        options[i] = html.unescape(answers.pop())

    for option in options:
        opts.append(options.get(option))

    return render_template("index.html", name=username, question=question, opts=opts)


@app.route("/submit", methods=["POST"])
def submit():
    global CORRECT_ANSWER
    if request.form.get("answer") == CORRECT_ANSWER:
        return redirect("/correct")
    else:
        return redirect("/incorrect")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application

