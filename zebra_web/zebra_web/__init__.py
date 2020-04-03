from flask import Flask, render_template, request, json, flash, redirect, url_for, jsonify 
from passlib.hash import sha256_crypt


userandpassword = sha256_crypt.encrypt("admin")
watch_data = []

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if sha256_crypt.verify(request.form['inputUserName'], userandpassword) and \
            sha256_crypt.verify(request.form['inputPassword'], userandpassword):
            return redirect(url_for('main'))
        else:
            flash('You entered the wrong credentials. Please try again', 'danger')
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/main')
def main():
    if request.method == 'POST':
       #mouse data sent over
       #Do Something Here 
       data=request.json

       
    else:
        return render_template('main.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return redirect(url_for('login'))

    return render_template('logout.html')

@app.route('/watch', methods = ['GET', 'POST'])
def get_messages():
    data = request.get_json()
    watch_data.append(data)
    return jsonify({'watch:': watch_data})

if __name__ == "__main__":
    app.run()