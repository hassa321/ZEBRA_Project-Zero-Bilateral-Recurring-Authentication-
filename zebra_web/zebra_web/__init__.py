from flask import Flask, render_template, request, json, flash, redirect, url_for, jsonify 
from passlib.hash import sha256_crypt

keys_pressed = []
keys_released = []
keys_mapped = {'1': 1, '2': 1, '3': 1, '!': 1, '@': 1, '#': 1, '4': 2, '5': 2, 
               '6': 2, '$': 2, '%': 2, '^': 2, '7': 3, '8': 3, '&': 3, '*': 3, 
               '9': 4, '0': 4, '(': 4, ')': 4, '-': 5, '_': 5, '=': 5, '+': 5, 
               'backspace': 5, 'q': 6, 'tab': 6, 'w': 7, 'e': 7, 'r': 7, 't': 8, 
               'y': 8, 'u': 9, 'i': 9, 'o': 9, 'p': 9, '[': 10, ']': 10, 
               '\\': 10, '{': 10, '}': 10, '|': 10, 'a': 11, 's': 11, 'd': 11, 
               'f': 12, 'g': 12, 'h': 12, 'j': 13, 'k': 13, 'l': 13, ';': 14, 
               "'": 14, '"': 14, ':': 14, 'enter': 14, 'z': 15, 'x': 15, 'c': 15, 
               'space': 16, 'b': 16, 'n': 16, 'm': 16, ',': 17, '.': 17, '/': 17, 
               '<': 17, '>': 17, '?': 17, 'arrowleft': 18, 'arrowright': 18, 
               'arrowup': 18, 'arrowdown': 18}
special_keys = ["shift", "control", "alt", "meta", "backspace", "arrowleft", "arrowright"]


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
    return render_template('main.html')


'''
data at the moment is a list of items in format as
{ "timestamp": timestamp, "action": "keypress", "key": event.key, "location": "right" }
'''
@app.route('/watch_data', methods = ['GET', 'POST'])
def watch_data():
    if request.method == 'POST':
       data=request.json
    

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

def splitKeyboardStrokes(data):
    for keyEvent in data:
        #"timestamp": timestamp, "action": "keyup", "key": event.key, "location": "left" 
        #Seperate keyEvents by Up or keypress
        #Timestamp, key side, key
        timestamp = keyEvent.get("timestamp")
        action = keyEvent.get("action")
        key = keyEvent.get("key")
        location = keyEvent.get("location")

        if action == "keypress":
            keys_pressed.append([timestamp, keys_mapped.get(key, 19), location])
            # if keyEvent.get("key") in ["Shift", "Control", "Alt"]:
            #     keys_pressed[-1].append(keyEvent.get("key"))
            # else:
            #     keys_pressed[-1].append("None")

        elif key not in special_keys:
            keys_released.append([timestamp, keys_mapped.get(key, 19), location])
            # keys_released.append([keyEvent.get("timestamp"), keyEvent.get("location"), keyEvent.get("key")])
            # if keyEvent.get("key") in ["Shift", "Control", "Alt"]:
            #     keys_released[-1].append(keyEvent.get("key"))
            # else:
            #     keys_released[-1].append("None")    

    return




if __name__ == "__main__":
    app.run()