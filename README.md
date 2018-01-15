# Facebook-ChatBot

Moody chatbot, who understands the tone of user's message, and replies accordingly.
Bot's mood is updated with every positive(+1) or negative(-1) message. User can return bot's mood by typing 'mood'. 
I used Facebook Messenger's webhook, and also IBM Watson's Tone Analyzer API and deployed to Heroku.


#### For example:
* user: I love you
* bot: Oh, that's very kind of you

* user: I hate you
* bot: I feel so bad about what you wrote

* user: that book is blue
* bot: Interesting. Ok.

#### mood
If user types 'mood', bot will return it's mood(positive, negative, neutral) along with the mood level number.
* user: mood
* bot: positive / Mood Level: 1

## Why don't you run it on your local machine?
### Just follow the instructions
* clone this repo
* install ngrok
* run ngrok server like: ```./ngrok http 5000```
* run flask development server like ```python3 main.py```
* create an any page on facebook.
* set a messenger webhook on developers.facebook.com and assign your newly created page with https(must be https, not http) url of ngrok server in terminal, and set ```chatBotToken``` as verify token
* Then, send a message to your page, and enjoy :)
