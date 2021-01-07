import random, datetime
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'secret'

grid = [{"full_name":"Farm",
         "id_name":"farm",         
         "message":"earns 10-20 golds",
         "min_gold":10,
         "max_gold":20},
        {"full_name":"Cave",
         "id_name":"cave",
         "message":"earns 5-10 golds",
         "min_gold":5,
         "max_gold":10},
        {"full_name":"House",
         "id_name":"house",
         "message":"earns 2-5 golds",
         "min_gold":2,
         "max_gold":5},
        {"full_name":"Casino",
         "id_name":"casino",
         "message":"earns/takes 0-50 golds",
         "min_gold":-50,
         "max_gold":50}]

getDict = { box['id_name']:box for box in grid }

def randInt(*vals):
    if len(vals) == 1:
        return int(random.random()*(vals[0]+1))
    elif len(vals) >= 2 and vals[1]>vals[0]:
        return int(random.random()*(vals[1]-vals[0]+1))+vals[0]
    return random.random()

@app.before_first_request
def activate_job():
    session['activities'] = []
    session['gold'] = 0

@app.route('/')
def index():
    global grid
    return render_template("index.html", grid=grid)

@app.route('/process_money', methods=['POST'])
def process_money():
    val = request.form['getVal']
    goldToAdd = randInt(getDict[val]['min_gold'], getDict[val]['max_gold'])
    session['gold']+=goldToAdd
    
    d = datetime.datetime.today()
    date = str(d.year)+'/'+str(d.month).zfill(2)+'/'+str(d.day).zfill(2)
    localTime = str(d.hour)+":"+str(d.minute)
    currTime = '('+date+" "+localTime+')'
    
    if val != 'casino':
        session['activities'].append(('text-green','Earned ' + str(goldToAdd) + ' golds from the ' + val + ' ' + currTime))
    else:
        if goldToAdd < 0:
            session['activities'].append(('text-red','Entered a ' + val + ' and lost ' + str(abs(goldToAdd)) + ' golds... Ouch.. ' + currTime))
        elif goldToAdd > 0:
            session['activities'].append(('text-green','Entered a ' + val + ' and earned ' + str(goldToAdd) + ' golds... Nice.. ' + currTime))
        else:
            session['activities'].append(('text-black','Entered a ' + val + ' and lost no golds ' + currTime))
    return redirect(url_for('index'))

if __name__=="__main__": app.run()