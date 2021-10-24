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
        self.player_text = ""  # current input from player
        self.used_letters = []
        self.over = False
        self.dark_theme = True
        self.language = "english"
        self.key_words = EN_DIC  # holds all key words depending on the active language

        self.images = {}

        self.play_button = Button("play", [200, 400], LETTER_SIZE)
        self.return_button = Button(" <", [0, 0], LETTER_SIZE)
        self.restart_button = Button("R", [50, 0], LETTER_SIZE)
        self.settings_button = Button("settings", [200, 450], LETTER_SIZE)
        self.help_button = Button("help", [200, 500], LETTER_SIZE)
        self.pt_button = Button("PT", [SCREEN_WIDTH - 100, 200], LETTER_SIZE2)
        self.en_button = Button("EN", [SCREEN_WIDTH - 200, 200], LETTER_SIZE2)
        self.theme_button = Button("ON", [SCREEN_WIDTH - 100, 300], LETTER_SIZE2)

        self.buttons = [self.play_button, self.return_button, self.restart_button,
                        self.settings_button, self.help_button, self.pt_button, self.en_button]

        self.en_button.press()

    def start(self):
        '''Starts the game.'''
        self.word = Word()
        self.menu = False
        self.hangman = Hangman()
        self.over = False

        # print(self.word.letters) #print the solution

    def update_buttons(self):
        '''Changes all the buttons display to the current language (if needed).'''
        self.buttons = [self.play_button, self.return_button, self.restart_button,
                        self.settings_button, self.help_button, self.pt_button, self.en_button]
        for i in self.buttons:
            i.set_text(self.key_words[i.text], self.dark_theme)

    def get_images(self):
        if self.dark_theme:
            self.images["menu"] = pygame.image.load(
                "../assets/images/menu.png")
            self.images["1"] = pygame.image.load(
                "../assets/images/hangman1.png")
            self.images["2"] = pygame.image.load(
                "../assets/images/hangman2.png")
            self.images["3"] = pygame.image.load(
                "../assets/images/hangman3.png")
            self.images["4"] = pygame.image.load(
                "../assets/images/hangman4.png")
            self.images["5"] = pygame.image.load(
                "../assets/images/hangman5.png")
            self.images["6"] = pygame.image.load(
                "../assets/images/hangman6.png")
            self.images["7"] = pygame.image.load(
                "../assets/images/hangman7.png")
            self.images["8"] = pygame.image.load(
                "../assets/images/hangman8.png")
            self.images["help_english"] = pygame.image.load(
                "../assets/images/help_english.png")
            self.images["help_portuguese"] = pygame.image.load(
                "../assets/images/help_portuguese.png")
        else:
            self.images["menu"] = pygame.image.load(
                "../assets/images/menu_light.png")
            self.images["1"] = pygame.image.load(
                "../assets/images/hangman1_light.png")
            self.images["2"] = pygame.image.load(
                "../assets/images/hangman2_light.png")
            self.images["3"] = pygame.image.load(
                "../assets/images/hangman3_light.png")
            self.images["4"] = pygame.image.load(
                "../assets/images/hangman4_light.png")
            self.images["5"] = pygame.image.load(
                "../assets/images/hangman5_light.png")
            self.images["6"] = pygame.image.load(
                "../assets/images/hangman6_light.png")
            self.images["7"] = pygame.image.load(
                "../assets/images/hangman7_light.png")
            self.images["8"] = pygame.image.load(
                "../assets/images/hangman8_light.png")
            self.images["help_english"] = pygame.image.load(
                "../assets/images/help_english_light.png")
            self.images["help_portuguese"] = pygame.image.load(
                "../assets/images/help_portuguese_light.png")

    def render(self, win):
        '''Renders everything to the screen.'''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        font2 = pygame.font.Font(FONT_NAME, LETTER_SIZE2)

        self.update_buttons()
        self.get_images()

        #####Render the menu#####
        if self.menu:
            menu_img = self.images["menu"]
            win.blit(menu_img, (0, 0))

            # menu play button
            self.play_button.center()
            self.play_button.render(win)

            # menu settings button
            self.settings_button.center()
            self.settings_button.render(win)

            # menu help button
            self.help_button.center()
            self.help_button.render(win)

        elif self.help:
            image = self.images["help_%s" % (str(self.language))]
            win.blit(image, (0, 0))

            self.return_button.render(win)

            # Render the tab title
            text = font.render(self.key_words["help"], True, WHITE)
            win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

        else:
            win.fill(BLACK)
            if not self.dark_theme: win.fill(WHITE)
            self.return_button.render(win)

            if self.settings:
                # Render the tab title
                if self.dark_theme: text = font.render(self.key_words["settings"], True, WHITE)
                else: text = font.render(self.key_words["settings"], True, BLACK)
                win.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

                # Render the language options
                if self.dark_theme: text = font2.render(self.key_words["language"], True, WHITE)
                else: text = font2.render(self.key_words["language"], True, BLACK)
                win.blit(text, (50, 200))
                self.pt_button.allign_right(50)
                self.pt_button.render(win)
                self.en_button.set_x(self.pt_button.coords[0] - 100)
                self.en_button.render(win)

                if self.dark_theme: text = font2.render(self.key_words["dark mode"], True, WHITE)
                else: text = font2.render(self.key_words["dark mode"], True, BLACK)
                win.blit(text, (50, 300))
                self.theme_button.allign_right(50)
                self.theme_button.render(win)

            elif self.playing:
                #####Render the alphabet in the bottom#####
                pos_x = SCREEN_WIDTH / 2 - LETTER_SIZE * (len(ALPHABET) / 4)
                pos_y = 500
                for i in ALPHABET:
                    if self.dark_theme: text = font.render(i, 1, WHITE)
                    else: text = font.render(i, 1, BLACK)
                    if i in self.word.used_letters:
                        if self.dark_theme: text = font.render(i, 1, BLACK)
                        else: text = font.render(i, 1, WHITE)
                    elif i in self.word.filled_letters:
                        if self.dark_theme: text = font.render(i, 1, WHITE)

                    win.blit(text, (pos_x - (text.get_width() / 2), pos_y))
                    pos_x += LETTER_SIZE
                    if i == 'm':
                        pos_y += LETTER_SIZE + 1
                        pos_x = SCREEN_WIDTH / 2 - \
                            LETTER_SIZE * (len(ALPHABET) / 4)

                ######Draw the hangman#####
                self.hangman.draw(win, self.images)

                #####Draw the playing word#####
                self.word.draw(win, self.dark_theme)

                #####Display game over messages#####
                if self.hangman.state == 8:
                    text = font.render(self.key_words["lost"], True, WHITE)
                    win.blit(text, (SCREEN_WIDTH / 2 -
                             text.get_width() / 2, 360))
                elif not '_' in self.word.filled_letters:
                    text = font.render(self.key_words["won"], 1, WHITE)
                    win.blit(text, (SCREEN_WIDTH / 2 -
                             text.get_width() / 2, 360))

                #####Render buttons####
                self.restart_button.render(win)

        pygame.display.update()

    def handle_envents(self):
        '''Handles key and mouse presses.

           @return - False if the exit button was pressed else True.
        '''
        mouse = pygame.mouse.get_pos()
        # print(mouse)
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
                    self.theme_button.click(mouse, click[0])
                if self.playing:
                    self.restart_button.click(mouse, click[0])

            if event.type == pygame.KEYDOWN:
                if not self.menu:
                    if len(self.player_text) < 1:
                        self.player_text = pygame.key.name(event.key).lower()
                        if self.player_text not in ALPHABET:
                            self.player_text = ""

        return True

    def run_logic(self):
        '''Executes the game logic.'''
        if self.menu:
            # start the game button
            if self.play_button.clicked:
                self.play_button.clicked = False
                self.menu = False
                self.playing = True
                self.start()

            # settings button
            if self.settings_button.clicked:
                self.settings_button.clicked = False
                self.menu = False
                self.settings = True

            if self.help_button.clicked:
                self.help_button.clicked = False
                self.menu = False
                self.help = True

        else:
            # return to menu button
            if self.return_button.clicked:
                self.return_button.clicked = False
                self.menu = True
                self.playing = False
                self.settings = False
                self.help = False

            if self.settings:
                if self.language == "english":
                    self.en_button.press()
                else:
                    self.pt_button.press()

                if self.pt_button.clicked:
                    self.language = "portuguese"
                    self.key_words = PT_DIC

                if self.en_button.clicked:
                    self.language = "english"
                    self.key_words = EN_DIC

                if self.theme_button.check():
                    if self.dark_theme:
                        self.theme_button.set_text("OFF", self.dark_theme)
                        self.dark_theme = False
                    else:
                        self.theme_button.set_text("ON", self.dark_theme)
                        self.dark_theme = True

            if self.playing:
                # restart button
                if self.restart_button.check():
                    self.start()

                # handling the guessing
                if len(self.player_text) == 1 and not self.over:
                    if not self.word.fill(self.player_text):
                        self.used_letters.append(self.player_text)
                        if self.hangman.state < 8:
                            self.hangman.state += 1
                self.player_text = ""

                if self.hangman.state == 8 or not '_' in self.word.filled_letters:
                    self.over = True
                    self.word.solve()
