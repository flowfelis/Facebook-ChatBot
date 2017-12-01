# Facebook-ChatBot
## What is it?
It's a Facebook ChatBot with mood, who understands the tone of user's message, and replies accordingly.
I used Facebook Messenger's webhook, and also IBM Watson's Tone Analyzer API.

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
