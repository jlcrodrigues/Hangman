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

        self.play_button = Button("play", [200, 400], LETTER_SIZE)
        self.return_button = Button(" <", [0, 0], LETTER_SIZE)
        self.restart_button = Button("R", [50, 0], LETTER_SIZE)
        self.settings_button = Button("settings", [200, 450], LETTER_SIZE)
        self.help_button = Button("help", [200, 500], LETTER_SIZE)
        self.pt_button = Button("PT", (SCREEN_WIDTH - 100, 200), LETTER_SIZE2)
        self.en_button = Button("EN", (SCREEN_WIDTH - 200, 200), LETTER_SIZE2)

        self.buttons = [self.play_button, self.return_button, self.restart_button, self.settings_button, self.help_button, self.pt_button, self.en_button]

        self.en_button.press()

    def start(self):
        '''Starts the game.'''
        self.word = Word()
        self.menu = False
        self.hangman = Hangman()
        self.over = False

        #print(self.word.letters) #print the solution

    def update_buttons(self):
        '''Changes all the buttons display to the current language (if needed).'''
        self.buttons = [self.play_button, self.return_button, self.restart_button, self.settings_button, self.help_button, self.pt_button, self.en_button]
        for i in self.buttons:
            i.set_text(self.key_words[i.text])

    def render(self, win):
        '''Renders everything to the screen.'''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        font2 = pygame.font.Font(FONT_NAME, LETTER_SIZE2)    

        self.update_buttons()

        #####Render the menu#####
        if self.menu:
            menu_img = pygame.image.load("../assets/images/menu.png")
            win.blit(menu_img, (0,0))

            #menu play button
            self.play_button.center()
            self.play_button.render(win)

            #menu settings button
            self.settings_button.center()
            self.settings_button.render(win)

            #menu help button
            self.help_button.center()
            self.help_button.render(win)

        elif self.help:
                image = pygame.image.load('../assets/images/help_%s.png' % (str(self.language)))
                win.blit(image, (0, 0))

                self.return_button.render(win)
            
                #Render the tab title
                text = font.render(self.key_words["help"], True, WHITE)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))
        
        else:
            win.fill(BLACK)
            self.return_button.render(win)

            if self.settings:
                #Render the tab title
                text = font.render(self.key_words["settings"], True, WHITE)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

                #Render the language options
                text = font2.render(self.key_words["language"], True, WHITE)
                win.blit(text, (50, 200))
                self.pt_button.render(win)
                self.en_button.render(win)

            elif self.playing: 
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
                elif not '_' in self.word.filled_letters:
                    text = font.render(self.key_words["won"], 1, WHITE)
                    win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))

                #####Render buttons####
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
            if self.play_button.clicked:
                self.play_button.clicked = False
                self.menu = False
                self.playing = True
                self.start()

            #settings button
            if self.settings_button.clicked:
                self.settings_button.clicked = False
                self.menu = False
                self.settings = True

            if self.help_button.clicked:
                self.help_button.clicked = False
                self.menu = False
                self.help = True

        else:
            #return to menu button
            if self.return_button.clicked:
                self.return_button.clicked = False
                self.menu = True
                self.playing = False
                self.settings = False
                self.help = False

            if self.settings:
                if self.language == "english": self.en_button.press()
                else: self.pt_button.press()
                
                if self.pt_button.clicked:
                    self.language = "portuguese"
                    self.key_words = PT_DIC

                if self.en_button.clicked:
                    self.language = "english"
                    self.key_words = EN_DIC

            if self.playing:
                #restart button
                if self.restart_button.clicked:
                    self.start()

                #handling the guessing
                if len(self.player_text) == 1 and not self.over:
                    if not self.word.fill(self.player_text):
                        self.used_letters.append(self.player_text)
                        if self.hangman.state < 8: self.hangman.state += 1
                self.player_text = ""
                    
                if self.hangman.state == 8 or not '_' in self.word.filled_letters:
                    self.over = True
                    self.word.solve()
