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

**Side-note**: We will use Mac OS X and run our app on Desktop for this example.

However, feel free to run this app from any os and path as you like.

### Just follow the instructions below:

1. **clone** this repo
  * go to your terminal and type `cd Desktop` and `git clone https://github.com/flowfelis/Facebook-ChatBot.git`
2. install **ngrok** by clicking [here](https://ngrok.com/download). Locate ngrok file (on your downloads folder propably).
  * ngrok will provide us a url on the web which tunnels to our localhost. We can use that url for facebook api webhook as we will see soon after.
  * move ngrok file to Desktop for convenience.  
  * run ngrok server like: ```./ngrok http 5000``` . but before make sure you are on your Desktop path.
3. run **flask** development server like ```python3 main.py``` in your terminal, make sure you are in Desktop/Facebook-ChatBot/ folder.
* Login to your personal **facebook** profile, and create a page. This page will represent the bot.
* Create a profile on [https://developers.facebook.com](https://developers.facebook.com) if you don't have
* Create a new app with Messenger       set a messenger webhook on developers.facebook.com and assign your newly created page with https(must be https, not http) url of ngrok server in terminal, and set ```chatBotToken``` as verify token
* Then, send a message to your page, and enjoy :)
