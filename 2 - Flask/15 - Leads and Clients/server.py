from flask import Flask, render_template, redirect, url_for, request, session, flash, Response
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "a"
mysql = connectToMySQL('codingdojo')

@app.before_first_request
def activate_job():
    session['leads'] = mysql.query_db("SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS label, COUNT(leads.leads_id) AS y FROM sites JOIN clients ON clients.client_id = sites.client_id LEFT JOIN leads ON leads.site_id=sites.site_id GROUP BY clients.client_id ORDER BY COUNT(leads.leads_id) DESC")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__": app.run()