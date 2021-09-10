import pygame
from word import Word
from hangman import Hangman
from config import *
from button import Button

class Game:
    def __init__(self):
        self.menu = True
        self.player_text = "" #current input from player
        self.used_letters = []
        self.over = False
        self.play_button = Button("Play", [200, 400])
        self.return_button = Button(" <", [0, 0])

    def start(self):
        self.word = Word()
        self.menu = False
        self.hangman = Hangman()
        self.over = False

        print(self.word.letters)

    def render(self, win):
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)    

        #####Render the menu#####
        if self.menu:
            menu_img = pygame.image.load("../assets/menu.png")
            win.blit(menu_img, (0,0))

            #menu play button
            self.play_button.set_x(SCREEN_WIDTH / 2 - self.play_button.width / 2)
            self.play_button.render(win)

        else:
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
                
                win.blit(text, (pos_x + (text.get_width() / 2), pos_y))         
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
                text = font.render('You lose!', True, WHITE)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))
            if not '_' in self.word.filled_letters:
                text = font.render('You win!', 1, WHITE)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 360))

            #####Render buttons####

            self.return_button.render(win)

            #game over buttons
            if self.over:
                text = font.render("Menu", True, WHITE)
                text = font.render("Restart", True, WHITE)

            
        
        pygame.display.update()


    def handle_envents(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                #self.play_button.click(mouse)
                pass

            click = pygame.mouse.get_pressed()

            if self.menu: self.play_button.click(mouse, click[0])
            self.return_button.click(mouse, click[0])
            
            if event.type == pygame.KEYDOWN:
                if not self.menu:
                    #handle lowercase and uppercase
                    if len(self.player_text) < 1 :
                        self.player_text = pygame.key.name(event.key).lower()
                        if self.player_text not in ALPHABET: self.player_text = ""
 
    def run_login(self):
        '''Executes the game logic.'''
        if self.menu:
            if self.play_button.pressed:
                self.menu = False
                self.start()
        else:
            if self.return_button.pressed:
                self.menu = True
            if len(self.player_text) == 1 and not self.over:
                #print("ENTER")
                if not self.word.fill(self.player_text):
                    self.used_letters.append(self.player_text)
                    if self.hangman.state < 8: self.hangman.state += 1
            self.player_text = ""
                
            if self.hangman.state == 8 or not '_' in self.word.filled_letters:
                self.over = True

                    