from flask import Flask, render_template, redirect, url_for, request, session, flash
import random

app = Flask(__name__)
app.secret_key = 'secret'

def rps(p1, p2):
    if p1 == p2:
        return 'ties'
    if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        return 'wins'
    return 'losses'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process/<choice>', methods=['POST'])
def result(choice):
    choices = ['rock','paper','scissors']
    cpuChoice = choices[int(random.random()*(len(choices)))]
    session[rps(choice, cpuChoice)]+=1
    return redirect(url_for('index'))

if __name__=="__main__": app.run()