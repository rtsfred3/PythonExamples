import random
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.before_first_request
def activate_job():
    session['val'] = random.randrange(1,101)
    print(session['val'])

@app.route('/', methods=['GET', 'POST'])
def index():
    global form
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == session['val']:
            return render_template("index.html", form_id="hide", box_right='show', box_wrong='hide')
        elif guess > session['val']:
            return render_template("index.html", form_id="show", box_right='hide', box_wrong='show', hint="Too High!")
        elif guess < session['val']:
            return render_template("index.html", form_id="show", box_right='hide', box_wrong='show', hint="Too Low!")        
    return render_template("index.html", form_id="show", box_right='hide', box_wrong='hide')

@app.route('/reset')
def destroy():
    session['val'] = random.randrange(1,101)
    print(session['val'])
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run()