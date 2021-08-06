import pygame
#from main import win
from config import *
class Hangman:
    def __init__(self):
        self.state = 0

    def isDead(self):
        if self.state == 8:
            return True
        return False
        

    def draw(self):
        image = pygame.image.load('images/%s.jpg' %str(self.state))
        #win.blit(image, (0, 0))
        pass
