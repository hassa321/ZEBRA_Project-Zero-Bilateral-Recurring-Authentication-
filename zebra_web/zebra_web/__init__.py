from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/showLogin')
def showLogin():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    _userName = request.form['inputUserName']
    _password = request.form['inputPassword']
 
    if _userName == 'admin' and _password == 'password':
        # return main()
        return json.dumps({'html':'<span>Credentials match !!</span>'})
    else:
        # flash("wrong password!!")
        return json.dumps({'html':'<span>Wrong credentials</span>'})

if __name__ == "__main__":
    app.run()