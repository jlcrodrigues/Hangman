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
    icon = pygame.image.load("../assets/images/icon.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    game = Game()

    run = True
    while run:
        clock.tick(60)

        #Render everything to the screen
        game.render(win)

        #Handle key presses and check if the window was closed
        run = game.handle_envents()

        #Execute all the game logic
        game.run_logic()

    pygame.quit()
    
if __name__ == '__main__':
    main()
