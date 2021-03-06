import pygame
from word import Word
from hangman import Hangman
from config import *
from button import Button
from bar import Bar


class Game:
    def __init__(self):
        #Current displaying window booleans
        self.menu = True
        self.settings = False
        self.playing = False
        self.help = False
        self.pre_play = False

        #Game logic
        self.player_text = ""  # current input from player
        self.used_letters = []
        self.over = False
        self.streak = 0
        with open("../assets/stats/balance.txt", "r") as input_file:
                self.balance = int(input_file.readlines()[0])

        #Window and display
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.volume_sfx = 0.5
        self.volume_music = 0.5
        self.dark_theme = True
        self.language = "english"
        self.key_words = EN_DIC  # holds all key words depending on the active language
        self.theme = "all"
        self.themes = ["all", "animals", "capitals", "countries", "hardw"]
        self.difficulty = "normal"
        self.difficulties = ["easy", "normal", "hard"]
        self.images = {}

        #Buttons and bars
        self.play_button = Button("play", [200, 400], LETTER_SIZE)
        self.start_button = Button("start", [200, 500], LETTER_SIZE)
        self.return_button = Button(" <", [0, 0], LETTER_SIZE)
        self.restart_button = Button("../assets/images/restart.png", [50, 5], LETTER_SIZE, True)
        self.settings_button = Button("settings", [200, 450], LETTER_SIZE)
        self.help_button = Button("help", [200, 500], LETTER_SIZE)
        self.pt_button = Button("PT", [self.width - 100, 200], LETTER_SIZE2)
        self.en_button = Button("EN", [self.width - 200, 200], LETTER_SIZE2)
        self.theme_button = Button("ON", [self.width - 100, 300], LETTER_SIZE2)
        self.right_button1 = Button(">", [0, 0], LETTER_SIZE)
        self.right_button2 = Button(">", [0, 0], LETTER_SIZE)
        self.left_button1 = Button("<", [0, 0], LETTER_SIZE)
        self.left_button2 = Button("<", [0, 0], LETTER_SIZE)
        self.aid_button = Button("?", [0, 0], LETTER_SIZE)

        self.sfx_bar = Bar([400, 500], 150, 0.5)
        self.music_bar = Bar([400, 400], 150, 0.5)

        self.buttons = [self.play_button, self.return_button, self.restart_button,
                        self.settings_button, self.help_button, self.pt_button, 
                        self.en_button, self.start_button, self.right_button1,
                        self.right_button2, self.left_button1, self.left_button2,
                        self.aid_button]

        self.en_button.press()

        #Sounds
        pygame.mixer.init()
        self.music_playing = False
        self.winning_sound = pygame.mixer.Sound("../assets/sounds/win.mp3")
        self.lose_sound = pygame.mixer.Sound("../assets/sounds/lose.mp3")
        pygame.mixer.music.load("../assets/sounds/menu.mp3")
        self.game_over_played = False
        

    def start(self):
        '''Starts the game.'''
        self.word = Word(self.theme, self.language, self.themes)
        self.menu = False
        self.playing = True
        self.hangman = Hangman()
        self.over = False
        self.game_over_played = False

        if self.difficulty == "easy":
            for _ in range(int(self.word.length / 5)):
                self.word.solve_letter()

        #print(self.word.letters) #print the solution

    def update_buttons(self):
        '''Changes all the buttons display to the current language (if needed).'''
        self.buttons = [self.play_button, self.return_button, self.restart_button,
                        self.settings_button, self.help_button, self.pt_button,
                        self.en_button, self.start_button, self.right_button1,
                        self.right_button2, self.left_button1, self.left_button2,
                        self.aid_button]
        for i in self.buttons:
            i.set_text(self.key_words[i.text], self.dark_theme)
            i.set_volume(self.volume_sfx)

    def write_stats(self):
        '''Updates the current balance to memory.'''
        with open("../assets/stats/balance.txt", "w") as input_file:
                input_file.write(str(self.balance))

    def get_images(self):
        '''Updates the images according to the selected theme.'''
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

    def render_menu(self, win):
        '''Renders the menu tab.
        
            @win - The game window.
        '''
        menu_img = self.images["menu"]
        win.blit(menu_img, (self.width / 2 - 300, self.height / 2 - 300))

        # menu play button
        self.play_button.center(self.width)
        self.play_button.set_y(self.height / 2 + 100)
        self.play_button.render(win)

        # menu settings button
        self.settings_button.center(self.width)
        self.settings_button.set_y(self.height / 2 + 150)
        self.settings_button.render(win)

        # menu help button
        self.help_button.center(self.width)
        self.help_button.set_y(self.height / 2 + 200)
        self.help_button.render(win)

    def render_help(self, win):
        '''Renders the help tab.
        
            @win - The game window.
        '''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        image = self.images["help_%s" % (str(self.language))]
        win.blit(image, (self.width / 2 - 300, self.height / 2 - 400))

        self.return_button.render(win)

        # Render the tab title
        text = font.render(self.key_words["help"], True, WHITE)
        win.blit(text, (self.width / 2 - text.get_width() / 2, 0))

    def render_settings(self, win):
        '''Renders the settings tab.
        
            @win - The game window.
        '''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        font2 = pygame.font.Font(FONT_NAME, LETTER_SIZE2)
        
        # Render the tab title
        if self.dark_theme: text = font.render(self.key_words["settings"], True, WHITE)
        else: text = font.render(self.key_words["settings"], True, BLACK)
        win.blit(text, (self.width / 2 - text.get_width() / 2, 0))

        # Render the language options
        if self.dark_theme: text = font2.render(self.key_words["language"], True, WHITE)
        else: text = font2.render(self.key_words["language"], True, BLACK)
        win.blit(text, (50, 200))
        self.pt_button.allign_right(50, self.width)
        self.pt_button.render(win)
        self.en_button.set_x(self.pt_button.coords[0] - 100)
        self.en_button.render(win)

        if self.dark_theme: text = font2.render(self.key_words["dark mode"], True, WHITE)
        else: text = font2.render(self.key_words["dark mode"], True, BLACK)
        win.blit(text, (50, 300))
        self.theme_button.allign_right(50, self.width)
        self.theme_button.render(win)

        if self.dark_theme: text = font2.render(self.key_words["music"], True, WHITE)
        else: text = font2.render(self.key_words["music"], True, BLACK)
        win.blit(text, (50, 400))
        self.music_bar.allign_right(50, self.width)
        self.music_bar.render(win, self.dark_theme)

        if self.dark_theme: text = font2.render(self.key_words["sfx"], True, WHITE)
        else: text = font2.render(self.key_words["sfx"], True, BLACK)
        win.blit(text, (50, 500))
        self.sfx_bar.allign_right(50, self.width)
        self.sfx_bar.render(win, self.dark_theme)

    def render_playing(self, win):
        '''Renders the playing tab.
        
            @win - The game window.
        '''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)

        #####Render the alphabet in the bottom#####
        pos_x = self.width / 2 - LETTER_SIZE * (len(ALPHABET) / 4) + 20
        #the extra 20 are added because each letter only fills half of the
        #available size which would leave space to the right
        pos_y = self.height - 100
        for i in ALPHABET:
            if self.dark_theme: text = font.render(i, 1, WHITE)
            else: text = font.render(i, 1, BLACK)
            if i in self.word.used_letters or i in self.word.filled_letters:
                if self.dark_theme: text = font.render(i, 1, BLACK)
                else: text = font.render(i, 1, WHITE)

            win.blit(text, (pos_x - (text.get_width() / 2), pos_y))
            pos_x += LETTER_SIZE
            if i == 'm':
                pos_y += LETTER_SIZE + 1
                pos_x = self.width / 2 - \
                    LETTER_SIZE * (len(ALPHABET) / 4) + 20

        ######Draw the hangman#####
        self.hangman.draw(win, self.images, self.width)

        #####Draw the playing word#####
        self.word.draw(win, self.dark_theme, self.width, self.height)

        #####Display game over messages#####
        if self.hangman.state == 8:
            if self.dark_theme: text = font.render(self.key_words["lost"], True, WHITE)
            else: text = font.render(self.key_words["lost"], True, BLACK)
            win.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 + 60))
        elif not '_' in self.word.filled_letters:
            if self.dark_theme: text = font.render(self.key_words["won"], 1, WHITE)
            else: text = font.render(self.key_words["won"], 1, BLACK)
            win.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 + 60))

        #####Render buttons#####
        self.restart_button.render(win)
        self.aid_button.allign_right(20, self.width)
        self.aid_button.set_y(self.height / 2 - 160)
        self.aid_button.render(win)

        #####Render the streak#####
        if self.streak > 0:
            if self.dark_theme: text = font.render(str(self.streak), True, WHITE)
            else: text = font.render(str(self.streak), True, BLACK)
            win.blit(text, (20, self.height / 2 - 160))

        #####Render the balance#####
        if self.dark_theme: text = font.render(str(self.balance), True, WHITE)
        else: text = font.render(str(self.balance), True, BLACK)
        win.blit(text, (self.width - len(str(self.balance)) * 20 - 20, 0))

    def render_pre_play(self, win):
        '''Renders the pre_play tab.
        
            @win - The game window.
        '''
        font = pygame.font.Font(FONT_NAME, LETTER_SIZE)
        font2 = pygame.font.Font(FONT_NAME, LETTER_SIZE2)
        
        # Render the theme options
        if self.dark_theme: text = font.render(self.key_words["theme"], True, WHITE)
        else: text = font.render(self.key_words["theme"], True, BLACK)
        win.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - 200))

        if self.dark_theme: text = font2.render(self.key_words[self.theme], True, WHITE)
        else: text = font2.render(self.key_words[self.theme], True, BLACK)
        win.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - 140))

        self.right_button1.set_x(self.width / 2 + 150)
        self.right_button1.set_y(self.height / 2 - 140)
        self.right_button1.render(win)
        self.left_button1.set_x(self.width / 2 - 150)
        self.left_button1.set_y(self.height / 2 - 140)
        self.left_button1.render(win)

        # Render the difficulty options
        if self.dark_theme: text = font.render(self.key_words["difficulty"], True, WHITE)
        else: text = font.render(self.key_words["difficulty"], True, BLACK)
        win.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 - 40))

        if self.dark_theme: text = font2.render(self.key_words[self.difficulty], True, WHITE)
        else: text = font2.render(self.key_words[self.difficulty], True, BLACK)
        win.blit(text, (self.width / 2 - text.get_width() / 2, self.height / 2 + 20))

        self.right_button2.set_x(self.width / 2 + 150)
        self.right_button2.set_y(self.height / 2 + 20)
        self.right_button2.render(win)
        self.left_button2.set_x(self.width / 2 - 150)
        self.left_button2.set_y(self.height / 2 + 20)
        self.left_button2.render(win)

        self.start_button.center(self.width)
        self.start_button.set_y(self.height - 100)
        self.start_button.render(win)
    
    def render(self, win):
        '''Renders the current tab.
        
            @win - The game window.
        '''
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()

        self.update_buttons()
        self.get_images()

        win.fill(BLACK)
        if not self.dark_theme: win.fill(WHITE)

        if self.menu:
            self.render_menu(win)

        elif self.help:
            self.render_help(win)

        else:
            win.fill(BLACK)
            if not self.dark_theme: win.fill(WHITE)
            self.return_button.render(win)

            if self.settings:
                self.render_settings(win)

            elif self.playing:
                self.render_playing(win)

            elif self.pre_play:
                self.render_pre_play(win)

        pygame.display.update()

    def handle_envents(self):
        '''Handles key and mouse presses.

           @return - False if the exit button was pressed else True.
        '''
        mouse = pygame.mouse.get_pos()
        # print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.write_stats()
                return False

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 600:
                    width = 600
                if height < 600:
                    height = 600
                win = pygame.display.set_mode((width,height), pygame.RESIZABLE)

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
                    self.sfx_bar.drag(mouse, click[0])
                    self.music_bar.drag(mouse, click[0])
                if self.playing:
                    self.restart_button.click(mouse, click[0])
                    self.aid_button.click(mouse, click[0])
                if self.pre_play:
                    self.start_button.click(mouse, click[0])
                    self.right_button1.click(mouse, click[0])
                    self.right_button2.click(mouse, click[0])
                    self.left_button1.click(mouse, click[0])
                    self.left_button2.click(mouse, click[0])

            if event.type == pygame.KEYDOWN:
                if self.playing:
                    if len(self.player_text) < 1:
                        self.player_text = pygame.key.name(event.key).lower()
                        if self.player_text not in ALPHABET:
                            self.player_text = ""

                    if event.key == pygame.K_RETURN:
                        if not self.over: self.streak = 0
                        self.start()

        return True

    def run_logic(self):
        '''Executes the game logic.'''
        if self.menu:
            # start the game button
            if self.play_button.clicked:
                self.play_button.clicked = False
                self.menu = False
                self.pre_play = True

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
                if self.playing: pygame.mixer.music.stop()
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

                self.volume_sfx = self.sfx_bar.pos
                self.sfx_bar.set_volume(self.sfx_bar.pos)
                self.volume_music = self.music_bar.pos

            if self.playing:
                # restart button
                if self.restart_button.check():
                    if not self.over: self.streak = 0
                    self.start()

                if self.aid_button.check():
                    if self.balance >= 5:
                        self.balance -= 5
                        self.word.solve_letter()

                # handling the guessing
                if len(self.player_text) == 1 and not self.over:
                    if not self.word.fill(self.player_text):
                        self.used_letters.append(self.player_text)
                        if self.hangman.state < 8:
                            self.hangman.state += 1
                            if self.difficulty == "hard": self.hangman.state += 1
                self.player_text = ""

                if self.hangman.state == 8 :
                    self.over = True
                    self.streak = 0
                    self.word.solve()

                if not '_' in self.word.filled_letters:
                    self.over = True
                    if not self.game_over_played: 
                        self.streak += 1
                        self.balance += int(self.streak * 0.5)

            if self.pre_play:
                if self.start_button.check():
                    self.pre_play = False
                    pygame.mixer.music.stop()
                    self.start()

                if self.right_button1.check():
                    self.theme = self.themes[min(len(self.themes) - 1, self.themes.index(self.theme) + 1)]
                if self.left_button1.check():
                    self.theme = self.themes[max(0, self.themes.index(self.theme) - 1)]
                if self.right_button2.check():
                    self.difficulty = self.difficulties[min(len(self.difficulties) - 1, self.difficulties.index(self.difficulty) + 1)]
                if self.left_button2.check():
                    self.difficulty = self.difficulties[max(0, self.difficulties.index(self.difficulty) - 1)]

    def play_sounds(self):
        '''Plays the game's sounds.'''
        pygame.mixer.music.set_volume(self.volume_music)
        if self.playing:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("../assets/sounds/play.mp3")
                pygame.mixer.music.play(-1)

            if not self.game_over_played:
                if self.hangman.state == 8:
                    self.winning_sound.set_volume(self.volume_sfx)
                    pygame.mixer.Sound.play(self.winning_sound)
                    self.game_over_played = True
                elif not '_' in self.word.filled_letters:
                    self.lose_sound.set_volume(self.volume_sfx)
                    pygame.mixer.Sound.play(self.lose_sound)
                    self.game_over_played = True
        else:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("../assets/sounds/menu.mp3")
                pygame.mixer.music.play(-1)