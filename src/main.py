from game import Game
from hangman import Hangman
from player import Player
from word import Word
from config import *
import pygame

def main():

    pygame.init()

    win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    pygame.display.set_caption("Hangman")

    
    word = Word()


    run = True
    while run:
        word.draw(win)

        #these should be in game later
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)

    pygame.quit()
    
if __name__ == '__main__':
    main()
