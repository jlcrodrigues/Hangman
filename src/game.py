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
        
        self.word.draw(win)
        if self.menu:
            win.blit(MENU, (0,0))
        if len(self.player_text) <= 1:
            text= font.render(self.player_text, 1, WHITE)
            win.blit(text, (100, 100)) #player text

        #draw the used letters
        pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(abc) / 4)
        pos_y = 4 * SCREEN_HEIGHT / 5
        for i in abc:
            text = font.render(i, 1, WHITE)
            if i in self.word.used_letters:
                text = font.render(i, 1, RED)
            elif i in self.word.filled_letters:
                text = font.render(i, 1, GREEN)
            
            win.blit(text, (pos_x + (text.get_width() / 2), pos_y))         
            pos_x += LETTER_SIZE
            if i == 'm': 
                pos_y += LETTER_SIZE + 1
                pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(abc) / 4)
        
        #for i in self.word.used_letters:            
         #   text = font.render(i, 1, WHITE)
          #  win.blit(text, (pos_x + (text.get_width() / 2), 4*SCREEN_HEIGHT / 5))         
           # pos_x += LETTER_SIZE

        #draw the hangman
        
        #draw win or lose
        if self.hangman.state == 8:
            text = font.render( 'YOU LOSE', 1, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - len('YOU LOSE') * LETTER_SIZE, 1/8 * SCREEN_HEIGHT))
        if not '_' in self.word.filled_letters:
            text = font.render( 'YOU WIN', 1, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - len('YOU WIN') * LETTER_SIZE/2, 1/8 * SCREEN_HEIGHT))

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
            print(self.hangman.state)

                    