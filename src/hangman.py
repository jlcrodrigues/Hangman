import pygame

from config import *
class Hangman:
    def __init__(self):
        self.state = 1

    def isDead(self):
        if self.state == 8:
            return True
        return False
        

    def draw(self, win):
        #print('../assets/hangman_%s.png' % (str(self.state)))
        image = pygame.image.load('../assets/hangman_%s.png' % (str(self.state)))
        win.blit(image, (0, 0))
        pass
