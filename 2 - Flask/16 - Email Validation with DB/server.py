from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import connectToMySQL

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "a"
mysql = connectToMySQL('codingdojo')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_email', methods=['POST'])
def add_email():
    global EMAIL_MATCH
    
    if EMAIL_MATCH.match(request.form['email']):
        emails = mysql.query_db("SELECT * FROM emails")
        email = [row['email'] for row in emails]
        if request.form['email'] in email:
            query = "UPDATE emails SET updated_at=NOW() WHERE email=%(email)s"
            data = { 'email': request.form['email'] }
            mysql.query_db(query, data)
        else:
            query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
            data = { 'email': request.form['email'] }
            mysql.query_db(query, data)
            session['email'] = request.form['email']
        emails = mysql.query_db("SELECT * FROM emails")
        return render_template("success.html", emails=emails)
    
    flash("Email is not valid!")
    return redirect('/')

if __name__ == "__main__": app.run()