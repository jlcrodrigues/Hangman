import random
from config import list_words

class Word:
    def __init__(self):
        #maybe we read from a text file here and choose a random word
        #theme could be a parameter
        self.letters=random.choice(list_words)
        
        #test
        #self.letters = 'MOSCOWM'
        
        self.filled_letters = ['_' for x in self.letters ]
        self.used_letters =[]

    def draw(self, letter):
        if letter in self.used_letters:
            print('Invalid input, try again')
        elif letter in self.letters:
            for i in range(len(self.letters)):
                if self.letters[i] == letter:
                    self.filled_letters[i] = letter
            #indexes = self.letters.find(letter)
            return True
        else:
            self.used_letters.append(letter)
            return False
        #checks if the letter input has already been used or if it is
        #correct or wrong. It needs to change the hangman status after
