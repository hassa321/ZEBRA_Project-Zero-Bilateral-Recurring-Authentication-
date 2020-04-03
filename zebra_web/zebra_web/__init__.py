from flask import Flask, render_template, request, json, flash, redirect, url_for, jsonify
from passlib.hash import sha256_crypt
import numpy as np
import time, random

watch_data = []
keys_presssed = []
keys_released = []
sequences = []
predictions = []
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
       splitKeyboardStrokes(data)
       
    return ''
    

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
    key_press = []
    key_release = []
    for keyEvent in data:
        #"timestamp": timestamp, "action": "keyup", "key": event.key, "location": "left" 
        #Seperate keyEvents by Up or keypress
        #Timestamp, key side, key
        timestamp = keyEvent.get("timestamp")
        action = keyEvent.get("action")
        key = keyEvent.get("key")
        location = keyEvent.get("location")

        if action == "keypress": 
            key_press.append([timestamp, keys_mapped.get(key, 19), location])
            # if keyEvent.get("key") in ["Shift", "Control", "Alt"]:
            #     keys_pressed[-1].append(keyEvent.get("key"))
            # else:
            #     keys_pressed[-1].append("None")

        elif key not in special_keys:
            key_release.append([timestamp, keys_mapped.get(key, 19), location])
            # keys_released.append([keyEvent.get("timestamp"), keyEvent.get("location"), keyEvent.get("key")])
            # if keyEvent.get("key") in ["Shift", "Control", "Alt"]:
            #     keys_released[-1].append(keyEvent.get("key"))
            # else:
            #     keys_released[-1].append("None")    
    keys_pressed = key_press[1:]
    keys_released = key_release[0:-1]

def create_dummy():
    milliseconds = int(round(time.time() * 1000))
    x = random.uniform(1.5, 1.9)
    y = random.uniform(1.5, 1.9)
    z = random.uniform(1.5,1.9)
    watch_data.append([milliseconds,x,y,z])




def map_sequences(keys_pressed,keys_released,watch_data):
    #watch_should be in form [ [ x, y, z, timestamp] ...]
    #keys pressed released in form [ [ timestamp, key, location]]

    for i in range(len(keys_pressed)):
        start = int(keys_released[i][0])
        end = int(keys_pressed[i][0])
        key = keys_pressed[i][1]

        sequence = []

        while len(watch_data) != 0:
            # We want to remove the line so we dont have to iterate trough everything again
            line = watch_data.pop(0)
            if line == ['']:
                continue 

            time, acc_x, acc_y, acc_z = line[0], line[1], line[2], line[3]

            current_time = int(time)

            if (current_time < start):
                continue 
            if (current_time >= end):
                break 

            sequence.append([float(acc_x), float(acc_y), float(acc_z)])
        sequences.append(sequence)
        predictions.append(key)
    return sequences

def padding(sequences):
    max_seq_3 = max(sequences,key=len)
    print(max_seq_3)
    max_len = len(max_seq_3)
    print(max_len)

    padded_sequences = []
    for sequence in sequences:
        while (len(sequence) < max_len):
            sequence.append([0, 0, 0])
        np.stack(sequence)
        padded_sequences.append(sequence)
    np_sequences = np.stack(padded_sequences)

    print(np_sequences.shape)

def predict(batch_of_10):
  pickled = open("/loc/to/weights.pickle","r")
  rfc = np.pickle.loads(pickled)
  
  prediction = rfc.predict(batch_of_10)
  if prediction >= 0.2:
    return True
  return False   

    


if __name__ == "__main__":
    app.run()