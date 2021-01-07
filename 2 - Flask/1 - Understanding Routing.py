from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say(name):
    return 'Hi ' + name

@app.route('/repeat/<num>/<string>')
def repeat(num, string):
    arr = []
    for i in range(int(num)):
        arr.append(string)
    return "<br/>".join(arr)

if __name__=="__main__":
    app.run()