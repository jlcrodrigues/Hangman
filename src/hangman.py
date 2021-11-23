from config import *

class Hangman:
    def __init__(self):
        self.state = 0

    def isDead(self):
        '''Returns True if the Hangman is dead.'''
        return self.state == 8

    def draw(self, win, images, width):
        '''Renders the current hangman state.
        
            @win - The game window.
            @images - Current displaying images according to theme.
            @width - The window's width.
        '''
        if self.state:
            image = images["%s" % (str(self.state))]
            win.blit(image, (width / 2 - 177, 0))
