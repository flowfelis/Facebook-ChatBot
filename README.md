# Facebook-ChatBot
## What is it?
It's a Facebook ChatBot with mood, who understands the tone of user's message, and replies accordingly.
Bot's mood is updated with every positive(+1) or negative(-1) message. User can return bot's mood by typing 'mood'. 
I used Facebook Messenger's webhook, and also IBM Watson's Tone Analyzer API and uploaded on Heroku. Let me know if you would like to try!


#### For example:
* user: I love you
* bot: Oh, that's very kind of you

* user: I hate you
* bot: I feel so bad about what you wrote

* user: that book is blue
* bot: Interesting. Ok.

#### mood
If user types 'mood', bot will return it's mood(positive, negative, neutral) with the mood level number.
* user: mood
* bot: positive / Mood Level: 1

## How to run it locally?
* clone this repo
* install ngrok
* run ngrok server like: ```./ngrok http 5000```
* run flask development server like ```python3 main.py```
* create an any page on facebook.
* set a messenger webhook on developers.facebook.com and assign your newly created page with https(must be https, not http) url of ngrok server in terminal, and set ```chatBotToken``` as verify token
* Then, send a message to your page, and enjoy :)
