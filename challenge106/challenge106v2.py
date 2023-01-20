#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
import html
import requests
import random

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
    question = html.unescape(question_dict['question'])  # question to send
    CORRECT_ANSWER = question_dict['correct_answer']
    answers = [question_dict['correct_answer']]
    answers.extend(question_dict['incorrect_answers'])
    letters = 'ABCD'
    options = {}
    opts = []
    for i in range(4):
        # if len(answers) > 1:
        #     rand = random.randint(0, (len(answers) - 1))
        # else:
        #     rand = 0
        # if len(answers) > 0:
        options[letters[i]] = html.unescape(answers.pop())

    for let in options:
        opts.append(options.get(let))

    correct = question_dict['correct_answer']

    return render_template("index.html", name=username, question=question, opts=opts)


@app.route("/submit", methods=["POST"])
def submit():
    global CORRECT_ANSWER
    print(request.form.get("answer"))
    print(CORRECT_ANSWER)
    if request.form.get("answer") == CORRECT_ANSWER:
        return redirect(url_for("correct"))
    else:
        return redirect(url_for("incorrect"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # runs the application

