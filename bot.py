import os

class Bot():
    """Bot class"""
    def __init__(self, result):
        try:
            self.result = result[0]
        except Exception as e:
            self.result = None
        self.answers = {
            'positive': 'Oh, that\'s very kind of you',
            'neutral': 'Interesting. Ok.',
            'negative': 'I feel so bad about what you wrote',
            }
        self.positiveEmotions = ['joy']
        self.negativeEmotions = ['anger', 'fear', 'sadness']
        self.path = os.getcwd() + '/moodCounter.txt'

    def reply(self):
        """This is returning the final answer"""
        if self.result in self.negativeEmotions:
            return self.answers['negative']
        elif self.result in self.positiveEmotions:
            return self.answers['positive']
        else:
            return self.answers['neutral']

    def evalMood(self):
        """Evaluate Mood (positive, negative, neutral)"""
        moodLevel = self.readFile()
        if self.result in self.negativeEmotions:
            moodLevel -= 1
        elif self.result in self.positiveEmotions:
            moodLevel += 1
        self.writeFile(moodLevel)

    def getMood(self):
        moodLev = self.readFile()
        if moodLev > 0:
            return 'positive'
        elif moodLev < 0:
            return 'negative'
        else:
            return 'neutral'

    def readFile(self):
        handle = open(self.path, 'r')
        content = handle.read()
        handle.close()
        return int(content)

    def writeFile(self, content):
        handle = open(self.path, 'w')
        handle.write(str(content))
        handle.close()
