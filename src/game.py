import pygame
from word import Word
from hangman import Hangman
from config import *

class Game:
    def __init__(self):
        self.word = Word() 
        #self.number_of_players = number_of_players
        self.menu = False
        self.is_writing = False
        self.player_text = "" #current input from player
        self.used_letters = []
        self.hangman = Hangman()
        
        print(self.word.letters)

    def render(self, win):
        font = pygame.font.SysFont((FONT_NAME), LETTER_SIZE)
        #MENU = pygame.image.load('insert_menu_file_name_here.png')
        self.word.draw(win)
        if self.menu:
            win.blit(MENU, (0,0))
        if len(self.player_text) <= 1:
            text= font.render(self.player_text, 1, WHITE)
            win.blit(text, (100, 100)) #player text

        #draw the used letters
        pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len("abcdefghijklmnopqrstuvwxyz") / 2)
        for i in "abcdefghijklmnopqrstuvwxyz":
            text = font.render(i, 1, WHITE)
            if i in self.word.used_letters:
                text = font.render(i, 1, RED)
            elif i in self.word.filled_letters:
                text = font.render(i, 1, GREEN)
            
            win.blit(text, (pos_x + (text.get_width() / 2), 4*SCREEN_HEIGHT / 5))         
            pos_x += LETTER_SIZE
        
        #for i in self.word.used_letters:            
         #   text = font.render(i, 1, WHITE)
          #  win.blit(text, (pos_x + (text.get_width() / 2), 4*SCREEN_HEIGHT / 5))         
           # pos_x += LETTER_SIZE

        #draw the hangman

    def handle_envents(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #if menu:  if mouse in menu boxes: code
                #if coords_of_text_box.collidepoint(mouse):
                if True: #check for textbox
                    self.is_writing = True
                else:
                    self.is_writing = False
            
            if event.type == pygame.KEYDOWN:

                #handle lowercase and uppercase
                if self.is_writing and len(self.player_text) < 1 :
                    self.player_text = pygame.key.name(event.key)
                    print(self.player_text)
 
    def play(self):
        if self.is_writing:
            #print("rrr")

            #input is being taken when a key is pressed maybe we should wait for ENTER or something
            if len(self.player_text) == 1:
                #print("ENTER")
                if not self.word.fill(self.player_text):
                    self.used_letters.append(self.player_text)
                    self.hangman.state += 1
                self.player_text = ""
                
            if self.hangman.state == 8:
               #game over
                pass 

                    