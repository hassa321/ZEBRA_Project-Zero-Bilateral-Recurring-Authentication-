from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def start():
    return render_template('index.html')

@app.route('/signIn')
def signIn():
    return render_template('signIn.html')

@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run()