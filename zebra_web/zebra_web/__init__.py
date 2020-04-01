from flask import Flask, render_template, request, json, flash, redirect, url_for
import re


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['inputUserName'] != 'admin' or request.form['inputPassword'] != 'admin':
            flash('You entered the wrong credentials. Please try again', 'danger')
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('main'))
    return render_template('login.html', error=error)



@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
       #keyboardStrokes for Demo data sent over here
       #Do Something Here 
       data=request.json
       formattedKeyEvents= splitKeyboardStrokes(data)
       #mapSequences(formattedKeyEvents,watchdata)

       return 'success'
       
    else:
        
        return render_template('main.html')







@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return redirect(url_for('login'))

    return render_template('logout.html')







def splitKeyboardStrokes(data):
    locations = {"left": 0, "center": 1, "right": 2}
    special_keys = {"Shift": 1, "Control": 2, "Alt": 3, "None": 0}
    keys_pressed = []
    keys_released = []
    all_keys_used = []
    last_event = None
    
    for keyEvent in data:
        #Seperate keyEvents by Up or keypress
        #Timestamp, key side, key
        if keyEvent.get("action") == "keypress":

            keys_pressed.append([keyEvent.get("timestamp"), keyEvent.get("location"), keyEvent.get("key")])
        else:
            keys_released.append([keyEvent.get("timestamp"), keyEvent.get("location"), keyEvent.get("key")])    

    return [keys_released,keys_pressed]



def mapSequences():
# Go through the watch data and map each sequence with a key
# Sequence begins when a key is released until the next is pressed 
#not complete due to watch data not being able to be sent to server. 

    sequences=[]
    count = 0

























if __name__ == "__main__":
    app.run()