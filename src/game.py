import pygame
from word import Word
from config import *

class Game:
    def __init__(self):
        self.word = Word()  
        #self.number_of_players = number_of_players
        self.menu = False
        self.is_writing = False
        self.player_text = "" #current input from player

    def render(self, win):
        font = pygame.font.SysFont((FONT_NAME), LETTER_SIZE)
        #MENU = pygame.image.load('insert_menu_file_name_here.png')
        self.word.draw(win)
        if self.menu:
            win.blit(MENU, (0,0))
        if len(self.player_text) <= 1:
            text= font.render(self.player_text, 1, WHITE)
            win.blit(text, (100, 100)) #player text

    def handle_envents(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #if menu:  if mouse in menu boxes: code
                #if coords_of_text_box.collidepoint(mouse):
                if True:
                    self.is_writing = True
                else:
                    self.is_writing = False
            
            if event.type == pygame.KEYDOWN:
                if self.is_writing and len(self.player_text) < 1:
                    self.player_text = pygame.key.name(event.key)
 
    def play(self):
        if self.is_writing:
            print("Receiving")
                 
                    