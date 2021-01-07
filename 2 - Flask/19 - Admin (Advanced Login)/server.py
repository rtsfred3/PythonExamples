from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import connectToMySQL

NAME_MATCH = re.compile(r'.[^1-9\s]*')
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "a"
bcrypt = Bcrypt(app)
mysql = connectToMySQL('codingdojo')

@app.before_first_request
def activate_job():
    if not ('logged_in' in session.keys() and 'user' in session.keys()):
        session['logged_in'] = False
        session['user'] = {}

@app.route('/')
def index():
    if session['logged_in'] and not (session['user'] == {}):
        return redirect(url_for('success'))
    return render_template("index.html")

@app.route('/admin')
def admin():
    if session['logged_in'] and not (session['user'] == {}) and session['user']['privilege'] == 0:
        users = mysql.query_db("SELECT user_id, CONCAT(first_name, \" \", last_name) AS name, email, privilege FROM users;")
        return render_template("admin.html", users=users)
    elif session['logged_in'] and not (session['user'] == {}) and session['user']['privilege'] == 1:
        return redirect(url_for('success'))
    
    session['logged_in'] = False
    session['user'] = {}
    return redirect(url_for('index'))

@app.route('/user')
def user():
    if session['logged_in'] and not (session['user'] == {}) and session['user']['privilege'] == 1:
        return render_template("user.html")
    elif session['logged_in'] and not (session['user'] == {}) and session['user']['privilege'] == 0:
        return redirect(url_for('success'))
    
    session['logged_in'] = False
    session['user'] = {}
    return redirect(url_for('index'))

@app.route('/modify_user', methods=['POST'])
def modify_user():
    if session['logged_in'] and not (session['user'] == {}) and session['user']['privilege'] is 0:
        data = { 'user_id':int(request.form['user_id']) }
        user = mysql.query_db("SELECT user_id, CONCAT(first_name, \" \", last_name) AS name, email, privilege FROM users WHERE user_id=%(user_id)s;", data)[0]
        query = "UPDATE users SET privilege='"+str(abs(int(user['privilege'])-1))+"' WHERE user_id=%(user_id)s;"
        mysql.query_db(query, data)
        
    return redirect(url_for('success'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    query = "DELETE FROM users WHERE user_id=%(user_id)s;"
    data = { 'user_id':request.form['user_id'] }
    mysql.query_db(query, data)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    if session['logged_in'] and not (session['user'] == {}):
        session['user'] = mysql.query_db("SELECT user_id, first_name, last_name, CONCAT(first_name, \" \", last_name) AS name, email, privilege FROM users WHERE email=%(email)s;", { 'email':session['user']['email'] })[0]
        if session['user']['privilege'] == 0:
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('user'))
    return redirect(url_for('index'))

@app.route('/logoff', methods=['GET', 'POST'])
def logoff():
    session['logged_in'] = False
    session['user'] = {}
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    users = mysql.query_db("SELECT * FROM users")
    emails = [user['email'] for user in users]
    if request.form['email'] in emails:
        user = mysql.query_db("SELECT email, password FROM users WHERE email=%(email)s", {'email':request.form['email']})[0]
        if bcrypt.check_password_hash(user['password'], request.form['password']):
            session['logged_in'] = True
            session['user'] = mysql.query_db("SELECT user_id, first_name, last_name, CONCAT(first_name, \" \", last_name) AS name, email, privilege FROM users WHERE email=%(email)s;", { 'email':request.form['email'] })[0]
    return redirect(url_for('success'))

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['first_name']) < 3 or len(request.form['last_name']) < 3 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1 or request.form['password'] != request.form['confirm_password'] or (not EMAIL_MATCH.match(request.form['email']) and len(request.form['email']) > 0) or (len(request.form['password']) > 0 and len(request.form['password']) < 8 and request.form['password'] == request.form['confirm_password']):
        if len(request.form['email']) < 1:
            flash("Email cannot be empty!")
        
        if len(request.form['first_name']) < 1:
            flash("First name cannot be empty!")
        elif len(request.form['first_name']) <= 2:
            flash("First name must be more than two letters!")
        
        if len(request.form['last_name']) < 1:
            flash("Last Name cannot be empty!")
        elif len(request.form['last_name']) <= 2:
            flash("Last name must be more than two letters!")        
        
        if len(request.form['password']) < 1:
            flash("Password cannot be empty!")
        
        if len(request.form['confirm_password']) < 1:
            flash("Confirm Password cannot be empty!")
        
        if request.form['password'] != request.form['confirm_password']:
            flash("Passwords do not match!")
        
        if not EMAIL_MATCH.match(request.form['email']) and len(request.form['email']) > 0:
            flash("Invalid Email Address!")
        
        if len(request.form['password']) > 0 and len(request.form['password']) < 8 and request.form['password'] == request.form['confirm_password']:
            flash("Password does not meet the minimum length of 8 characters!")
        
        return redirect(url_for('index'))
    else:
        query = "INSERT INTO users (first_name, last_name, email, privilege, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(privilege)s, %(password)s, NOW(), NOW());"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'privilege': 1,
            'password': bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        }
        mysql.query_db(query, data)
        session['logged_in'] = True
        session['user'] = mysql.query_db("SELECT first_name, last_name, email FROM users WHERE email=%(email)s", {'email':request.form['email']})[0]
        flash("You successfully registered.")
            
        return redirect(url_for('success'))

if __name__=="__main__": app.run(host='0.0.0.0')