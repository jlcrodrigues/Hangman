import random
from config import list_words

class Word:
    def __init__(self):
        #maybe we read from a text file here and choose a random word
        #theme could be a parameter
        self.letters=[random.choice(list_words)]
        self.filled_letters = ['_' for x in self.letters ]

    def draw(self):
        pass
