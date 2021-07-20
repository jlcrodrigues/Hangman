import pygame
from word import Word
from config import *

class Game:
    def __init__(self):
        self.word = Word()  
        #self.number_of_players = number_of_players
        self.menu = True 

    def render(self, win):
        MENU = pygame.image.load('insert_menu_file_name_here.png')
        self.word.draw(win)
        if self.menu:
            win.blit(MENU, (0,0))

    def play(self):
        mouse = pygame.mouse.get_pos()
        font = pygame.font.SysFont(("trebuchetms"), LETTER_SIZE/2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #debug
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
                #if menu:  if mouse in menu boxes: code
                if coords_of_text_box.collidepoint(mouse):
                    active = True
            
            if event.type == pygame.KEYDOWN:
                if active:
                    self.word.letter = pygame.key.name(event.key)
                    text = font.render(self.word.letter, 1, WHITE)
                    win.blit(text, (text_x_coordinate, text_y_coordinate ))         
                    