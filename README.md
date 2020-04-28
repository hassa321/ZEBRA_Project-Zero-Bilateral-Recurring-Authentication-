# Csc490_Zebra_Project

## Locally Run
```
cd zebra_web

pip install passlib
pip install flask
pip install numpy
pip install -U scikit-learn
pip install joblib

$env:FLASK_APP = "zebra_web"
$env:FLASK_ENV = "development"

flask run
```

This document is a weekly log of the user stories we worked on. For further documentation regarding user story implementation and all references used, please refer to: 
https://colab.research.google.com/drive/19MWL_aAL_eJq_3pEL0GSBV5yBO6PHC4s

## Week 1 (Feb 7th, 2020)
### User Stories
* __Web App__ - Setting up Web App
* __Web App__ - Login Request Form
* __Web App__ - Verify Login (_without hashing_)
* __Web App__ - Main Page
* __Watch App__ - Collecting accelerometer and gyroscope data

#### Flask Installation
1. https://flask.palletsprojects.com/en/1.1.x/installation/#installation
2. https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

#### Folder Structure

1. https://exploreflask.com/en/latest/organizing.html
2. https://stackoverflow.com/questions/14415500/common-folder-file-structure-in-flask-app 
3. https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/
4. https://stackoverflow.com/questions/14415500/common-folder-file-structure-in-flask-app

#### Login page code inspiration
1. https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
2. https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
3. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/

#### Apple Watch app and Data Extraction tutorials and resources
1. https://medium.com/@jaewhyun/building-a-watchos-and-ios-app-using-coremotion-and-watchconnectivity-594bfe0839bf
2. https://heartbeat.fritz.ai/introduction-to-apple-watchkit-with-core-motion-tracking-jumping-jacks-259ee80d1210
3. https://developer.apple.com/documentation/coremotion


## Week 2 (Feb 14th, 2020)
### User Stories
* __Web App__ - Main Page
* __Web App__ - Log Out - Inactivity
* __Web App__ - Mouse Data Collection (_SCRAPPED_)

### References
#### MouseData Events Webpage Extraction tutorials and resources 
1. https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43796.pdf
2. https://developers.google.com/maps/documentation/javascript/events

#### AJAX Server Calls resources 
1. https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started
2. https://plainjs.com/javascript/ajax/send-ajax-get-and-post-requests-47/

#### Timeout
1. https://schier.co/blog/wait-for-user-to-stop-typing-using-javascript


## Week 3 (Feb 21st, 2020)
### User Stories
* __Watch App__ - Determining the type of user activity (_SCRAPPED_)

### References
#### User's Activity Type with Core Motion
1. https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager

## Week 4 (Feb 28th, 2020)
### User Stories
* __Training Machine Learning Model__ - Setting up
* __Training Machine Learning Model__ - Data Processing Functions (padding and sequencing)


### References
#### Research for classifier
1. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
2. https://www.datacamp.com/community/tutorials/random-forests-classifier-python

#### Additional Research papers
1. https://arxiv.org/pdf/1505.05779.pdf
2. https://chrisalbon.com/machine_learning/trees_and_forests/random_forest_classifier_example/
3. https://synrg.csl.illinois.edu/papers/mole.pdf

#### Hidden Markov Models (for distribution predictions) used in practice: 
1. http://csis.pace.edu/~ctappert/srd2015/2015PDF/b2.pdf
2. https://www.hindawi.com/journals/mpe/2012/986134/
3. Tutorial: https://www.researchgate.net/post/How_to_train_parameters_for_HMM_Gesture_Recognition10

#### Notes
- The idea is that the movements are what we are using to make or predictions on and the keyboard data can be used for checking which is used for training and validating our model
- We would use the model to predict what key should be pressed, and then when we do compare with the actual key pressed, it will return true/false


## Week 5 (Mar 6th, 2020)
### User Stories
* __Watch App__ - Sending accelerometer data to the server (_building HTTP request and sending it to a test server_)
* __Training Machine Learning Model__ - Data Processing Functions 
* __Training Machine Learning Model__ - Models (_Making the RNN and RFC_)

## Week 6 (Mar 13th, 2020)
### User Stories
* __Web App__ - Keyboard Data Collection (User Side)
* __Web App__ - Keyboard Data Collection (Server Side)
* __Training Machine Learning Model__ - Models - (_trying to improve accuracy_)

## Week 7 (Mar 20th, 2020)
### User Stories
* __Web App__ - Keyboard Data Collection (User Side)
* __Web App__ - Keyboard Data Collection (Server Side)

## Week 8 (March 27th, 2020)
### User Stories
* __Web App__ - Login Error Flashing
* __Web App__ - Get and Mapping Sequences
* __Web App__ - Set up prediction data
* __Web App__ - Making Prediction
* __Web App__ - Displaying Predictions
* __Web App__ - Logging watch and keyboard data
* __Web App__ - Parallelism

### References
#### Flash Message
1. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
2. https://pythonise.com/series/learning-flask/flask-message-flashing

#### Mouse and Keyboard timeout
1. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/

## Week 9 (April 4th, 2020)
### User Stories
* __Web App__ - Displaying Predictions
* __Web App__ - Verify Login
* __Web App__ - Making Prediction
* __Web App__ - Parallelism

#### Hashing Passwords
1. https://pythonprogramming.net/password-hashing-flask-tutorial/
