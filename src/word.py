import random
import pygame
from config import *

class Word:
    def __init__(self):
        #maybe we read from a text file here and choose a random word
        #theme could be a parameter
        self.letters = random.choice(list_words).lower()
        
        self.filled_letters = [x if x in "- " else '_' for x in self.letters] #the current state of the word
        self.length = len(self.letters)
        self.used_letters = []

    def solve(self):
        '''Fills the entire word.'''
        self.filled_letters = self.letters

    def fill(self, letter):
        '''Replaces a letter in the word being guessed if it belongs.
        
        Parameters:
        @letter - The letter the user wants to try to fill.

        @return - True if the letter belongs in the solution.
        '''
        if letter in self.used_letters: return True
        if letter in self.letters:
            for i in range(len(self.letters)):
                if self.letters[i] == letter.lower():
                    self.filled_letters[i] = letter.lower()
            return True
        elif letter.isalpha() and letter not in self.used_letters:
            self.used_letters.append(letter.lower())
        return False

    def draw(self, win):
        '''Renders each letter from filled_letters.'''
        pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (self.length / 2)
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        for i in self.filled_letters:
            text = font.render(i, True, WHITE, BLACK)
            win.blit(text, (pos_x - (text.get_width() / 2), SCREEN_HEIGHT / 2))         
            pos_x += LETTER_SIZE
