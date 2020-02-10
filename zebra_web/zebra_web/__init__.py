from flask import Flask, render_template, request, json, flash, redirect, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['inputUserName'] != 'admin' or request.form['inputPassword'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/main')
def main():
    if request.method == 'POST':
       #mouse data sent over 
       data=request.json
       
    else:
        return render_template('main.html')

'''
    At some point later on we need to implement some sort of logout feature so that
    when either the user wants to logout or is kicked off then we properly exist the
    'session'
'''
def logout():
    pass

if __name__ == "__main__":
    app.run()