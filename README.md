# Csc490_Zebra_Project
Zero Effort Continuous Authentication Implementation
Abstract
 	This is an implementation of ZEBRA, where when paired with an Apple watch, allows for continuous authentication of web apps. This adds an additional layer of security, beyond the initial login authentication. In the event that a user forgets to log off the application and steps away, the web page will automatically log the user off. Or if another user tries to use the web page under another user's credentials the session will be logged off. By training a neural net model we are able to analyze keystrokes to further verify whether the user interacting with the system is the same one that logged in. The model is fed information about the user such as their typing behaviours along with their hand movements which is retrieved from the Apple watch. The implementation we provide can be used by many web applications, especially those that wish to add another layer of security feature due to the sensitivity of their data. 

## References
---


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



#### MouseData Events Webpage Extraction tutorials and resources 
1. https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43796.pdf
2. https://developers.google.com/maps/documentation/javascript/events
#### AJAX Server Calls resources 
1. https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started
2. https://plainjs.com/javascript/ajax/send-ajax-get-and-post-requests-47/



#### Flash Message
1. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
2. https://pythonise.com/series/learning-flask/flask-message-flashing
#### Mouse and Keyboard timeout
1. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
