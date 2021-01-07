from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

fruits = [{'name':'Strawberry', 'quantity':10}, 
     {'name':'Raspberry', 'quantity':10},
     {'name':'Apple', 'quantity':10},
     {'name':'Pineapple', 'quantity':10},
     {'name':'Watermelon', 'quantity':10}]

@app.route('/')
def index():
    global fruits
    return render_template("index.html", fruits=fruits)

@app.route('/checkout', methods=['POST'])
def checkout():
    global fruits
    fruits_bought = {}
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    for fruit in fruits:
        fruits_bought[fruit['name']] = request.form[fruit['name']]
    return render_template("checkout.html", fruits=fruits, first_name=first_name, last_name=last_name, student_id=student_id, fruits_bought=fruits_bought)

if __name__=="__main__":
    app.run()