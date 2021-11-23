import random
import pygame
from config import *

class Word:
    def __init__(self, theme, language, themes):
        '''
            @theme - The game's word theme.
            @languange - The current game's language.
            @themes - All available themes.
        '''
        if theme != "all":
            with open("../assets/words/" + language + "/" + theme + ".txt", "r") as input_file:
                list_words = [x[:-1] for x in input_file.readlines()] #ignore the \n
        else:
            list_words = []
            for t in themes[1:]:
                with open("../assets/words/" + language + "/" + t + ".txt", "r") as input_file:
                    list_words += [x[:-1] for x in input_file.readlines()] #ignore the \n
        
        self.letters = random.choice(list_words).lower()
        
        self.filled_letters = [x if x in "- " else '_' for x in self.letters] #the current state of the word
        self.length = len(self.letters)
        self.used_letters = []
        

    def solve(self):
        '''Fills the entire word.'''
        self.filled_letters = self.letters

    def solve_letter(self):
        '''Fills a random letter.'''
        if '_' in self.filled_letters:
            self.fill(random.choice(list(set(self.letters) - set(self.filled_letters))))

    def fill(self, letter):
        '''Replaces a letter in the word being guessed if it belongs.
        
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

    def draw(self, win, dark_theme, width, height):
        '''Renders each letter from filled_letters.
        
            @win - The game window.
            @dark_theme - True if dark theme is on.
            @width - The window's width.
            @height - The window's height.
        '''
        pos_x = width / 2 - LETTER_SIZE * (self.length / 2) + 20
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        for i in self.filled_letters:
            if dark_theme: text = font.render(i, True, WHITE, BLACK)
            else: text = font.render(i, True, BLACK, WHITE)
            win.blit(text, (pos_x - (text.get_width() / 2), height / 2))         
            pos_x += LETTER_SIZE
