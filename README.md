# Csc490_Zebra_Project
Zero Effort Continuous Authentication Implementation
Abstract
 	This is an implementation of ZEBRA, where when paired with an Apple watch, allows for continuous authentication of web apps. This adds an additional layer of security, beyond the initial login authentication. In the event that a user forgets to log off the application and steps away, the web page will automatically log the user off. Or if another user tries to use the web page under another user's credentials the session will be logged off. By training a neural net model we are able to analyze keystrokes to further verify whether the user interacting with the system is the same one that logged in. The model is fed information about the user such as their typing behaviours along with their hand movements which is retrieved from the Apple watch. The implementation we provide can be used by many web applications, especially those that wish to add another layer of security feature due to the sensitivity of their data. 

## References
---
1. Acar, A., Aksu, H., Uluagac, A. S., & Akkaya, K. (2018, May). WACA: Wearable-assisted continuous authentication. In 2018 IEEE Security and Privacy Workshops (SPW) (pp. 264-269). IEEE. Retrieved from https://ieeexplore.ieee.org/abstract/document/8424658/
2. Aslam, F. A., Mohammed, H. N., Mohd, J. M., Gulamgaus, M. A., & Lok, P. S. (2015). Efficient Way Of Web Development Using Python And Flask. International Journal of Advanced Research in Computer Science, 6(2/
3. Chang, B., Liu, X., Li, Y., Wang, P., Zhu, W. T., & Wang, Z. (2017, June). Employing smartwatch for enhanced password authentication. In International Conference on Wireless Algorithms, Systems, and Applications (pp. 691-703). Springer, Cham. Retrieved from https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=4806&context=sis_research
4. Grujić, V. (2019, February 21). How to detect a sequence of keystrokes in JavaScript. Retrieved from https://medium.com/javascript-in-plain-english/how-to-detect-a-sequence-of-keystrokes-in-javascript-83ec6ffd8e93
5. Huhta, O., Shrestha, P., Udar, S., Juuti, M., Saxena, N., & Asokan, N. (2015). Pitfalls in designing zero-effort deauthentication: Opportunistic human observation attacks. Retrieved from https://arxiv.org/pdf/1505.05779.pdf
6. Hsiao, E. (2018, February 17). Introduction to Apple WatchKit with Core Motion - Tracking Jumping Jacks. Retrieved April 8, 2020, from https://heartbeat.fritz.ai/introduction-to-apple-watchkit-with-core-motion-tracking-jumping-jacks-259ee80d1210
7. Jingjing Li and Chunlin Peng, "jQuery-based Ajax general interactive architecture," 2012 IEEE International Conference on Computer Science and Automation Engineering, Beijing, 2012, pp. 304-306.
8. Maiti, A., Armbruster, O., Jadliwala, M., & He, J. (2016). Smartwatch-Based Keystroke Inference Attacks and Context-Aware Protection Mechanisms. Proceedings of the 11th ACM on Asia Conference on Computer and Communications Security - ASIA CCS 16. doi: 10.1145/2897845.2897905
9. Mare, S., Markham, A. M., Cornelius, C., Peterson, R., & Kotz, D. (2014, May). Zebra: Zero-effort bilateral recurring authentication. In 2014 IEEE Symposium on Security and Privacy (pp. 705-720). IEEE. Retrieved from https://ieeexplore.ieee.org/abstract/document/6956596
10. Miller, C. (2019, August 7). Apple Watch continues domination of the smartwatch industry, new Strategy Analytics data shows. Retrieved from https://9to5mac.com/2019/08/06/apple-watch-smartwatch-industry-q2/
Understanding JavaScript Mouse Events By Examples. (n.d.). Retrieved from https://www.javascripttutorial.net/javascript-dom/javascript-mouse-events/
11. Wang, H., Lai, T. T.-T., & Choudhury, R. R. (2015). MoLe. Proceedings of the 21st Annual International Conference on Mobile Computing and Networking - MobiCom 15. doi: 10.1145/2789168.2790121



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

### References
#### Research for classifier
1. https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
2. https://www.datacamp.com/community/tutorials/random-forests-classifier-python

#### Additional Research papers
1. https://arxiv.org/pdf/1505.05779.pdf
2. https://chrisalbon.com/machine_learning/trees_and_forests/random_forest_classifier_example/
3. https://synrg.csl.illinois.edu/papers/mole.pdf


#### Flash Message
1. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
2. https://pythonise.com/series/learning-flask/flask-message-flashing

#### Mouse and Keyboard timeout
1. https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/

