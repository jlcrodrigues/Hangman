import pygame
from word import Word

class Game:
    def __init__(self):
        self.word = Word()  
        #self.number_of_players = number_of_players

    def render(self, win):
        self.word.draw(win)

    def play(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #debug
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)

            
