import pygame
from word import Word
from hangman import Hangman
from config import *
from button import Button

class Game:
    def __init__(self):
        self.menu = True
        self.settings = False
        self.playing = False
        self.help = False
        self.player_text = "" #current input from player
        self.used_letters = []
        self.over = False
        self.language = "english"
        self.key_words = EN_DIC #holds all key words depending on the active language

        self.play_button = Button(self.key_words["play"], [200, 400], LETTER_SIZE)
        self.return_button = Button(" <", [0, 0], LETTER_SIZE)
        self.restart_button = Button("R", [50, 0], LETTER_SIZE)
        self.settings_button = Button(self.key_words["settings"], [200, 450], LETTER_SIZE)
        self.help_button = Button(self.key_words["help"], [200, 500], LETTER_SIZE)
        self.pt_button = Button("PT", (SCREEN_WIDTH - 100, 200), LETTER_SIZE2)
        self.en_button = Button("EN", (SCREEN_WIDTH - 200, 200), LETTER_SIZE2)
        self.en_button.press()

    def start(self):
        '''Starts the game.'''
        self.word = Word()
        self.menu = False
        self.hangman = Hangman()
        self.over = False

        #print(self.word.letters) #print the solution

    def render(self, win):
        '''Renders everything to the screen.'''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        font2 = pygame.font.Font(FONT_NAME, LETTER_SIZE2)    

        #####Render the menu#####
        if self.menu:
            menu_img = pygame.image.load("../assets/images/menu.png")
            win.blit(menu_img, (0,0))

            #menu play button
            self.play_button.set_x(SCREEN_WIDTH / 2 - self.play_button.width / 2)
            self.play_button.set_text(self.key_words["play"])
            self.play_button.render(win)

            #menu settings button
            self.settings_button.set_x(SCREEN_WIDTH / 2 - self.settings_button.width / 2)
            self.settings_button.set_text(self.key_words["settings"])
            self.settings_button.render(win)

            #menu help button
            self.help_button.set_x(SCREEN_WIDTH / 2 - self.help_button.width / 2)
            self.help_button.set_text(self.key_words["help"])
            self.help_button.render(win)

        elif self.settings:
            win.fill(BLACK)

            #Render the tab title
            text = font.render(self.key_words["settings"], True, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

            self.return_button.render(win)

            #Render the language options
            text = font2.render(self.key_words["language"], True, WHITE)
            win.blit(text, (50, 200))
            self.pt_button.render(win)
            self.en_button.render(win)

        elif self.help:
            image = pygame.image.load('../assets/images/help_%s.png' % (str(self.language)))
            win.blit(image, (0, 0))
           
            #Render the tab title
            text = font.render(self.key_words["help"], True, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

            self.return_button.render(win)

        elif self.playing:
            win.fill(BLACK)

            #####Render the alphabet in the bottom#####
            pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(ALPHABET) / 4)
            pos_y = 500
            for i in ALPHABET:
                text = font.render(i, 1, WHITE)
                if i in self.word.used_letters:
                    text = font.render(i, 1, BLACK)
                elif i in self.word.filled_letters:
                    text = font.render(i, 1, BLACK)
                
                win.blit(text, (pos_x - (text.get_width() / 2), pos_y))         
                pos_x += LETTER_SIZE
                if i == 'm': 
                    pos_y += LETTER_SIZE + 1
                    pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(ALPHABET) / 4)

            ######Draw the hangman#####
            self.hangman.draw(win)

            #####Draw the playing word#####
            self.word.draw(win)

            #####Display game over messages#####
            if self.hangman.state == 8:
                text = font.render(self.key_words["lost"], True, WHITE)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))
            if not '_' in self.word.filled_letters:
                text = font.render(self.key_words["won"], 1, WHITE)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))

            #####Render buttons####
            self.return_button.render(win)
            self.restart_button.render(win)
        
        pygame.display.update()


    def handle_envents(self):
        '''Handles key and mouse presses.
        
           @return - False if the exit button was pressed else True.
        '''
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            click = pygame.mouse.get_pressed()

            if self.menu: 
                self.play_button.click(mouse, click[0])
                self.settings_button.click(mouse, click[0])
                self.help_button.click(mouse, click[0])
            else:
                self.return_button.click(mouse, click[0])
                if self.settings:
                    self.pt_button.click(mouse, click[0])
                    self.en_button.click(mouse, click[0])
                if self.playing: 
                    self.restart_button.click(mouse, click[0])
            
            if event.type == pygame.KEYDOWN:
                if not self.menu:
                    if len(self.player_text) < 1 :
                        self.player_text = pygame.key.name(event.key).lower()
                        if self.player_text not in ALPHABET: self.player_text = ""
                    
        return True
 
    def run_logic(self):
        '''Executes the game logic.'''
        if self.menu:
            #start the game button
            if self.play_button.released: 
                self.play_button.released = False
                self.menu = False
                self.playing = True
                self.start()

            #settings button
            if self.settings_button.released:
                self.settings_button.released = False
                self.menu = False
                self.settings = True

            if self.help_button.released:
                self.help_button.released = False
                self.menu = False
                self.help = True

        else:
            #return to menu button
            if self.return_button.released: 
                self.return_button.released = False
                self.menu = True
                self.playing = False
                self.settings = False
                self.help = False

            if self.settings:
                if self.language == "english": self.en_button.press()
                else: self.pt_button.press()
                
                if self.pt_button.released:
                    self.pt_button.released = False
                    self.language = "portuguese"
                    self.key_words = PT_DIC

                if self.en_button.released:
                    self.en_button.released = False
                    self.language = "english"
                    self.key_words = EN_DIC

            if self.playing:
                #restart button
                if self.restart_button.released:
                    self.restart_button.released = False
                    self.start()

                #handling the guessing
                if len(self.player_text) == 1 and not self.over:
                    if not self.word.fill(self.player_text):
                        self.used_letters.append(self.player_text)
                        if self.hangman.state < 8: self.hangman.state += 1
                self.player_text = ""
                    
                if self.hangman.state == 8 or not '_' in self.word.filled_letters:
                    self.over = True
