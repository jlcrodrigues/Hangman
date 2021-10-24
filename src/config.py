'''Holds all constants needed for the game.'''

list_words = ['ola tudo bem-bem']

with open("../assets/words/english/animals.txt", "r") as input_file:
    list_words = [x[:-1] for x in input_file.readlines()] #ignore the \n


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

LETTER_SIZE = 40
LETTER_SIZE2 = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (127, 127, 127)
GREY1 = (190, 190, 190)

FONT_NAME = "../assets/fonts/font2.ttf"

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

EN_DIC = {" <" : " <", "EN" : "EN", "PT" : "PT", "R" : "R", "play" : "Play",
          "settings" : "Settings", "language" : "Language", "lost" : "You lose!",
          "won" : "You won!", "help" : "Help", "dark mode" : "Dark Mode", "ON" : "ON",
          "OFF" : "OFF", "../assets/images/restart.png" : "../assets/images/restart.png"}
PT_DIC = {" <" : " <", "EN" : "EN", "PT" : "PT", "R" : "R", "play" : "Jogar",
          "settings" : "Definicoes", "language" : "Idioma", "lost" : "Perdeste!",
          "won" : "Ganhaste!", "help" : "Ajuda", "dark mode" : "Modo Escuro", "ON" : "ON",
          "OFF" : "OFF", "../assets/images/restart.png" : "../assets/images/restart.png"}