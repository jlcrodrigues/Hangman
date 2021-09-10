import pygame
from word import Word
from hangman import Hangman
from config import *

class Game:
    def __init__(self):
        self.word = Word() 
        #self.number_of_players = number_of_players
        self.menu = False
        self.player_text = "" #current input from player
        self.used_letters = []
        self.hangman = Hangman()
        self.over = False
        
        print(self.word.letters)

    def render(self, win):
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        
        #####Draw the playing word#####
        self.word.draw(win)

        #####Render the menu#####
        if self.menu:
            win.blit(MENU, (0,0))

        
        if len(self.player_text) <= 1:
            text= font.render(self.player_text, 1, WHITE)
            win.blit(text, (100, 100)) #player text

        #####Render the alphabet in the bottom#####
        pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(ALPHABET) / 4)
        pos_y = 500
        for i in ALPHABET:
            text = font.render(i, 1, WHITE)
            if i in self.word.used_letters:
                text = font.render(i, 1, BLACK)
            elif i in self.word.filled_letters:
                text = font.render(i, 1, BLACK)
            
            win.blit(text, (pos_x + (text.get_width() / 2), pos_y))         
            pos_x += LETTER_SIZE
            if i == 'm': 
                pos_y += LETTER_SIZE + 1
                pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(ALPHABET) / 4)

        ######Draw the hangman#####
        self.hangman.draw(win)

        #####Display game over messages#####
        if self.hangman.state == 8:
            text = font.render('You lose!', True, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))
        if not '_' in self.word.filled_letters:
            text = font.render('You win!', 1, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))

        #####Render buttons####

        #go back to menu button
        text = font.render(' <', True, WHITE)
        win.blit(text, (0, 0))

        #game over buttons
        if self.over:
            text = font.render("Menu", True, WHITE)
            text = font.render("Restart", True, WHITE)


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
                if len(self.player_text) < 1 :
                    self.player_text = pygame.key.name(event.key).lower()
                    if self.player_text not in ALPHABET: self.player_text = ""
 
    def play(self):
        if len(self.player_text) == 1 and not self.over:
            #print("ENTER")
            if not self.word.fill(self.player_text):
                self.used_letters.append(self.player_text)
                if self.hangman.state < 8: self.hangman.state += 1
        self.player_text = ""
            
        if self.hangman.state == 8 or not '_' in self.word.filled_letters:
            self.over = True

                    