from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if not ('counter' in session.keys()):
        session['counter'] = 0
    if request.method == 'POST':
        session['counter'] += 1
        return redirect(url_for('index'))
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session['counter'] = 0
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run()