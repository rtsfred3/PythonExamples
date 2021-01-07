from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'secret'

locations = [{'id':'san_jose','name':'San Jose'},
             {'id':'seattle','name':'Seattle'},
             {'id':'los_angeles','name':'Los Angeles'},
             {'id':'dallas','name':'Dallas'},
             {'id':'tysons_corner','name':'Tysons Corner'},
             {'id':'chicago','name':'Chicago'},
             {'id':'tulsa','name':'Tulsa'},
             {'id':'east_bay','name':'East Bay'}]

languages = [{'id':'java','name':'Java'},
             {'id':'javascript','name':'Javascript'},
             {'id':'python','name':'Python'},
             {'id':'php','name':'PHP'},
             {'id':'ruby','name':'Ruby'},
             {'id':'c++','name':'C++'},
             {'id':'c','name':'C'},
             {'id':'c#','name':'C#'}]

locationsDict = { location['id']:location['name'] for location in locations }
languagesDict = { language['id']:language['name'] for language in languages }

@app.route('/')
def index():
    global languages
    global locations
    return render_template("index.html", languages=languages, locations=locations)

@app.route('/result', methods=['POST'])
def result():
    global languagesDict
    global locationsDict
    if len(request.form['name']) < 1 or len(request.form['comments']) > 120:
        if len(request.form['name']) < 1:
            flash("Name cannot be empty!")
        if len(request.form['comments']) > 120:
            flash("Comment cannot be more than 120 characters!")
        return redirect(url_for('index'))
    
    session['name'] = request.form['name']
    session['location'] = locationsDict[request.form['location']]
    session['language'] = languagesDict[request.form['language']]
    session['comments'] = request.form['comments']
    return render_template("result.html")

@app.route('/danger')
def danger():
    print("A user tried to visit /danger.  We have redirected the user to /")
    return redirect(url_for('index'))

if __name__=="__main__": app.run()