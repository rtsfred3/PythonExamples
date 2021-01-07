from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():   
    return render_template("survey.html")

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template("result.html", name=name, location=location, language=language, comments=comments)

@app.route('/danger')
def danger():
    print("A user tried to visit /danger.  We have redirected the user to /")
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run()