import pygame
from config import *


class Hangman:
    def __init__(self):
        self.state = 0

    def isDead(self):
        '''Returns True if the Hangman is dead.'''
        return self.state == 8

    def draw(self, win, images):
        '''Renders the current hangman state.'''
        if self.state:
            image = images["%s" % (str(self.state))]
            win.blit(image, (123, 0))
