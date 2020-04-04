from flask import Flask, render_template, request, json, flash, redirect, url_for, jsonify
from passlib.hash import sha256_crypt

# ML imports
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier


last_time = 0.0
all_keys_pressed = []
all_keys_released = []
watch_data = []

errors = []

authenticate = []
row = {"Key": "test", "Prediction": "test", "Authenticated": "test"}
authenticate.append(row)


keys_mapped = {'1': 1, '2': 1, '3': 1, '!': 1, '@': 1, '#': 1, '4': 2, '5': 2,
               '6': 2, '$': 2, '%': 2, '^': 2, '7': 3, '8': 3, '&': 3, '*': 3,
               '9': 4, '0': 4, '(': 4, ')': 4, '-': 5, '_': 5, '=': 5, '+': 5,
               'backspace': 5, 'q': 6, 'tab': 6, 'w': 7, 'e': 7, 'r': 7, 't': 8,
               'y': 8, 'u': 9, 'i': 9, 'o': 9, 'p': 9, '[': 10, ']': 10,
               '\\': 10, '{': 10, '}': 10, '|': 10, 'a': 11, 's': 11, 'd': 11,
               'f': 12, 'g': 12, 'h': 12, 'j': 13, 'k': 13, 'l': 13, ';': 14,
               "'": 14, '"': 14, ':': 14, 'enter': 14, 'z': 15, 'x': 15, 'c': 15,
               'space': 16, 'v': 16, 'b': 16, 'n': 16, 'm': 16, ',': 17, '.': 17, '/': 17,
               '<': 17, '>': 17, '?': 17, 'arrowleft': 18, 'arrowright': 18,
               'arrowup': 18, 'arrowdown': 18}
special_keys = ["shift", "control", "alt", "meta", "backspace", "arrowleft", "arrowright"]


userandpassword = sha256_crypt.encrypt("admin")
watch_data = []

app = Flask(__name__, static_folder='static')

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


@app.route('/print')
def printMsg():
    return render_template("error_log.html", errors=errors, len_err=len(errors))

@app.route('/pred')
def printpred():
    colnames=["Key", "Prediction", "Authenticated"]
    return render_template("predictions_log.html", colnames=colnames, preds=authenticate)


@app.route('/main')
def main():
    return render_template('main.html')


def _get_sequences(all_keys_pressed, all_keys_released):
    # Make sure that the watch data exists
    if not watch_data:
        return

    pressed = all_keys_pressed[:11]
    released = all_keys_released[:11]

    # Make sure the last item in the watch data is >= key released[-1][time]
    time_released = released[-1][0]
    time_watch = watch_data[-1][0]

    if time_watch < time_released:
        return

    errors.append("time match!!")
    # Remove the last and first
    pressed = pressed[1:]
    released = released[:-1]

    # Remove the batch from the list
    all_keys_pressed = all_keys_pressed[11:]
    all_keys_released = all_keys_released[11:]

    seq, ts = map_sequences(pressed, released)
    errors.append("len seq {0}".format(len(seq)))
    ys = padding(seq)

    errors.append("ys shape {0}".format(ys.shape))

    auth = predict(ys, ts)

    row = {"Key": ts, "Prediction": ys, "Authenticated": auth}

    authenticate.append(row)


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
        return render_template("log.html", display_data=(all_keys_pressed,all_keys_released))


def seperate_key_events(timestamp, event, key):
    if event == "keypress":
        all_keys_pressed.append([timestamp, keys_mapped.get(key, 19)])
    elif event == "keyup" and key not in special_keys:
        all_keys_released.append([timestamp, keys_mapped.get(key, 19)])

    if len(all_keys_pressed) > 11 and len(all_keys_released) > 11:
        _get_sequences(all_keys_pressed, all_keys_released)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return redirect(url_for('login'))

    return render_template('logout.html')


@app.route('/watch', methods = ['GET', 'POST'])
def get_messages():
    if request.method == 'POST':
        data = request.get_json()
        if (data):
            x = data["Ax"]
            y = data["Ay"]
            z = data["Az"]
            time_stamp = data["TimeStamp"]
            watch_data.append([time_stamp, x, y, z])
        return jsonify({"watch": watch_data})

    if request.method == 'GET':
        return render_template("log.html", display_data=watch_data)

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

        while len(watch_data) != 0:
            # We want to remove the line so we dont have to iterate trough everything again
            line = watch_data.pop(0)
            if line == ['']:
                errors.append("len of line in watch data is ['']: {0}".format(line))
                continue

            if len(line) < 4:
                errors.append("len of line in watch data is less than 4: {0}".format(line))
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
    return sequences, predictions


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
    errors.append("Shape = {0}".format(batch_of_10.shape))
    ys = batch_of_10.reshape((N,nx*ny))

    import os
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    path = os.path.join(SITE_ROOT, "static", "weights.joblib")
    model = joblib.load(path)
    acc = model.score(ys, ts) # ys MUST be of shape (10, 270, 3)
    errors.append("ACCC: {0}".format(acc))
    if acc >= 0.2:
        errors.append("YES")
        return True
    errors.append("NO")
    return False



if __name__ == "__main__":
    app.run()

