import random
import pygame
from config import *

class Word:
    def __init__(self):
        #maybe we read from a text file here and choose a random word
        #theme could be a parameter
        self.letters=random.choice(list_words)
        
        #test
        #self.letters = 'MOSCOWM'
        
        self.filled_letters = ['_' for x in self.letters]
        self.length = len(self.letters)
        self.used_letters =[]

    def play(self, letter): #wip
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

    def draw(self, win):
        '''Renders each letter from filled_letters to win.'''
        pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (self.length / 2)
        font = pygame.font.SysFont(("trebuchetms"), LETTER_SIZE)
        for i in self.filled_letters:            
            text = font.render(i, 1, WHITE)
            win.blit(text, (pos_x + (text.get_width() / 2), SCREEN_HEIGHT / 2))         
            pos_x += LETTER_SIZE
        pygame.display.update()
