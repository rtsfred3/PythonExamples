from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
@app.route('/play/')
@app.route('/play/<boxes>')
@app.route('/play/<boxes>/<color>')
def play(boxes="3", color="lightblue"):
    return render_template("play.html", boxes=int(boxes), color=color)

if __name__=="__main__":
    app.run()