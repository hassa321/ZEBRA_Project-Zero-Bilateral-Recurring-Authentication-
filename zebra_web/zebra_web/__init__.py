from flask import Flask, render_template, request, json, flash, redirect, url_for, jsonify
from passlib.hash import sha256_crypt

# ML imports
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
import threading

all_keys_pressed = {}
all_keys_released = {}
watch_data = {}
authenticate = {}


keys_mapped = {'1': 1, '2': 1, '3': 1, '!': 1, '@': 1, '#': 1, '4': 2, '5': 2,
               '6': 2, '$': 2, '%': 2, '^': 2, '7': 3, '8': 3, '&': 3, '*': 3,
               '9': 4, '0': 4, '(': 4, ')': 4, '-': 5, '_': 5, '=': 5, '+': 5,
               'backspace': 5, 'q': 6, 'tab': 6, 'w': 7, 'e': 7, 'r': 7, 't': 8,
               'y': 8, 'u': 9, 'i': 9, 'o': 9, 'p': 9, '[': 10, ']': 10,
               '\\': 10, '{': 10, '}': 10, '|': 10, 'a': 11, 's': 11, 'd': 11,
               'f': 12, 'g': 12, 'h': 12, 'j': 13, 'k': 13, 'l': 13, ';': 14,
               "'": 14, '"': 14, ':': 14, 'enter': 14, 'z': 15, 'x': 15, 'c': 15,
               ' ': 16, 'v': 16, 'b': 16, 'n': 16, 'm': 16, ',': 17, '.': 17, '/': 17,
               '<': 17, '>': 17, '?': 17, 'arrowleft': 18, 'arrowright': 18,
               'arrowup': 18, 'arrowdown': 18}
special_keys = {"keys": ["shift", "control", "alt", "meta", "backspace", "arrowleft", "arrowright", "arrowup", "arrowdown"]}


userandpassword = sha256_crypt.encrypt("admin")

app = Flask(__name__, static_folder='static')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

lock = threading.Lock()

import os
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
path = os.path.join(SITE_ROOT, "static", "weights.joblib")
model = joblib.load(path)


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


@app.route('/pred', methods=["GET"])
def printpred():

    colnames=["Keys", "Authenticated"]
    rows = authenticate["data"]
    return render_template("predictions_log.html", colnames=colnames, preds=rows)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return redirect(url_for('login'))

    return render_template('logout.html')


@app.route('/watch', methods = ['GET', 'POST'])
def get_watch():
    if request.method == 'POST':
        data = request.get_json()
        if (data):
            x = data["Ax"]
            y = data["Ay"]
            z = data["Az"]
            time_stamp = int(data["TimeStamp"])
            watch_data["data"].append([time_stamp, x, y, z])
        return jsonify({"watch": watch_data["data"]})

    if request.method == 'GET':
        len_watch = len(watch_data["data"])
        return render_template("log.html", data=watch_data["data"], len_data=len_watch)


@app.route('/keyboard', methods = ['GET', 'POST'])
def get_keystrokes():
    data = ''
    if request.method == 'POST':
        data = request.get_json()
        if (data):
            event = data["action"]
            key = data["key"].lower()
            timestamp = int(data["timestamp"])
            seperate_key_events(timestamp, event, key)
        return jsonify({'received' : data})
    if request.method == 'GET':
        pretty_print = ["Pressed {0}, Released {1}".format(p, r) for p, r in zip(all_keys_pressed["data"],all_keys_released["data"])]
        len_print = len(pretty_print)
        return render_template("log.html", data=pretty_print, len_data=len_print)


def seperate_key_events(timestamp, event, key):
    if event == "keypress" and key not in special_keys["keys"]:
        all_keys_pressed["data"].append([timestamp, keys_mapped.get(key, 19)])
    elif event == "keyup" and key not in special_keys["keys"]:
        all_keys_released["data"].append([timestamp, keys_mapped.get(key, 19)])

    if len(all_keys_pressed["data"]) > 11 and len(all_keys_released["data"]) > 11:
        ret = _get_sequences()

        if ret is not None:
            print ("about to predict")
            all_keys_pressed["data"] = all_keys_pressed["data"][11:]
            all_keys_released["data"] = all_keys_released["data"][11:]


            pressed, released = ret[0], ret[1]
            sequences, predictions = map_sequences(pressed, released)
            thread = threading.Thread(target=setup_predict, args=(sequences, predictions, lock))
            thread.start()


def _get_sequences():
    # Make sure that the watch data exists
    if watch_data["data"] == []:
        return None

    pressed = all_keys_pressed["data"][:11]
    released = all_keys_released["data"][:11]

    # Make sure the last item in the watch data is >= key released[-1][time]
    time_released = released[-1][0]
    time_watch = watch_data["data"][-1][0]

    if time_watch < time_released:
        return None

    # Remove the last and first
    pressed = pressed[1:]
    released = released[:-1]

    return (pressed, released)


def map_sequences(keys_pressed, keys_released):
    # watch should be in form [ [timestamp, x, y, z] ...]
    # keys pressed/released in form [ [ timestamp, key]]

    sequences = []
    predictions = []

    for i in range(len(keys_pressed)):
        start = int(keys_released[i][0])
        end = int(keys_pressed[i][0])
        key = keys_pressed[i][1]

        sequence = []

        while len(watch_data["data"]) != 0:
            # We want to remove the line so we dont have to iterate trough everything again
            line = watch_data["data"].pop(0)
            if line == [''] or len(line) < 4:
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

    return (sequences, predictions)

def setup_predict(sequences, predictions, lock):
    # With the introduction of threads we have this here
    ys = padding(sequences)

    auth = predict(ys, predictions)
    row = {"Keys": predictions, "Authenticated": auth}

    lock.acquire()
    try:
        authenticate["data"].append(row)
    except:
        lock.release()
    lock.release()

def padding(sequences):
    max_len = len(max(sequences,key=len))

    # If the sequence is greater than 270, just remove it
    while max_len > 270:
        sequences.remove(max_seq)
        max_len = len(max(sequences,key=len))

    max_len = 270

    padded_sequences = []
    for sequence in sequences:
        while (len(sequence) < max_len):
            sequence.append([0, 0, 0])
        np.stack(sequence)
        padded_sequences.append(sequence)
    np_sequences = np.stack(padded_sequences)

    return np_sequences

def predict(batch_of_10, ts):
    N, nx, ny = batch_of_10.shape
    ys = batch_of_10.reshape((N,nx*ny))

    acc = model.score(ys, ts) # ys MUST be of shape (10, 270, 3)
    print("Accuracy = {0}".format(acc))
    if acc >= 0.2:
        return True
    return False

def setup():
    all_keys_pressed["data"] = []
    all_keys_released["data"] = []
    watch_data["data"] = []
    authenticate["data"] = []

setup()


if __name__ == "__main__":
    app.run()
