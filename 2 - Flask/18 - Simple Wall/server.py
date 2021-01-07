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

@app.route('/send_message', methods=['POST'])
def send_message():
    query = "INSERT INTO messages (author_id, recipient_id, message, created_at) VALUES (%(author_id)s, %(recipient_id)s, %(message)s, NOW());"
    data = { 'author_id':int(request.form['author_id']),
             'recipient_id':int(request.form['recipient_id']),
             'message':request.form['message']
             }
    mysql.query_db(query, data)
    return redirect(url_for('success'))

@app.route('/delete_message', methods=['POST'])
def delete_message():
    query = "DELETE FROM messages WHERE message_id=%(message_id)s;"
    data = { 'message_id':int(request.form['message_id']) }
    mysql.query_db(query, data)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    if session['logged_in'] and not (session['user'] == {}):
        session['user']['num_messages_received'] = mysql.query_db("SELECT COUNT(messages.message_id) AS num_messages FROM messages JOIN users ON users.user_id=messages.recipient_id WHERE users.user_id=%(user_id)s GROUP BY messages.recipient_id", { 'user_id': session['user']['user_id'] })[0]['num_messages']
        
        session['user']['num_messages_sent'] = mysql.query_db("SELECT COUNT(messages.message_id) AS num_messages FROM messages JOIN users ON users.user_id=messages.author_id WHERE users.user_id=%(user_id)s GROUP BY messages.author_id", { 'user_id': session['user']['user_id'] })[0]['num_messages']
        
        session['user']['messages'] = mysql.query_db("SELECT messages.message_id, CONCAT(users.first_name, \" \", users.last_name) AS name, messages.message, TIMESTAMPDIFF(SECOND, messages.created_at, NOW()) AS age FROM messages JOIN users ON users.user_id=messages.author_id WHERE messages.recipient_id=%(user_id)s ORDER BY age ASC", { 'user_id': session['user']['user_id'] })
        
        session['users'] = mysql.query_db("SELECT user_id, first_name, last_name FROM users WHERE user_id!=%(user_id)s", { 'user_id': session['user']['user_id'] })
        return render_template("success.html")
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
            session['user'] = mysql.query_db("SELECT user_id, first_name, last_name, email FROM users WHERE email=%(email)s", {'email':request.form['email']})[0]
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        }
        mysql.query_db(query, data)
        session['logged_in'] = True
        session['user'] = mysql.query_db("SELECT first_name, last_name, email FROM users WHERE email=%(email)s", {'email':request.form['email']})[0]
        flash("You successfully registered.")
            
        return redirect(url_for('success'))

if __name__=="__main__": app.run(host='0.0.0.0')