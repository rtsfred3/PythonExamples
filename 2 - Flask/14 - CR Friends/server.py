from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = connectToMySQL('codingdojo')

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    return render_template("index.html", friends=all_friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__": app.run()