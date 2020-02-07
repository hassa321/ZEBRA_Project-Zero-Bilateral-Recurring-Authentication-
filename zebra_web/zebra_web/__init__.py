from flask import Flask, render_template, request, json, flash
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print ("fdgd")
        if request.form['inputUserName'] != 'admin' or request.form['inputPassword'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()