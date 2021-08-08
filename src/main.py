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
    clock = pygame.time.Clock()

    game = Game()

    run = True
    while run:
        clock.tick(60)
        game.render(win)
        game.handle_envents()
        game.play()

    
    pygame.quit()
    
if __name__ == '__main__':
    main()
