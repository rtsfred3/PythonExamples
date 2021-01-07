from flask import Flask, render_template, redirect, url_for, request, session, flash
import re

NAME_MATCH = re.compile(r'.[^1-9\s]*')
EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1 or request.form['password'] != request.form['confirm_password'] or (not EMAIL_MATCH.match(request.form['email']) and len(request.form['email']) > 0) or (len(request.form['password']) > 0 and len(request.form['password']) < 8 and request.form['password'] == request.form['confirm_password']):
        if len(request.form['email']) < 1:
            flash("Email cannot be empty!")
        
        if len(request.form['first_name']) < 1:
            flash("First Name cannot be empty!")
        
        if len(request.form['last_name']) < 1:
            flash("Last Name cannot be empty!")
        
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
    else:
        flash("Thanks for submitting your information.")
    return redirect(url_for('index'))

if __name__=="__main__": app.run()