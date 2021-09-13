import pygame
from config import *

class Button:
   def __init__(self, text, coords, letter_size):
      self.font = pygame.font.Font(FONT_NAME, letter_size)
      self.text = text    
      self.display = self.font.render(text, True, WHITE)
      self.coords = coords
      self.released = False
      self.pressed = False
      self.width = self.display.get_width()
      self.hitbox = [coords[0], coords[0] + self.display.get_width(), coords[1], coords[1] + self.display.get_height()]

   def render(self, win):
      '''Renders the button on the screen.'''
      win.blit(self.display, self.coords)

   def set_x(self, x):
      '''Changes the x coordinate of the button.'''
      self.coords[0] = x
      self.hitbox[0] = x
      self.hitbox[1] = x + self.display.get_width()

   def set_text(self, text):
      '''Changes the button's text.'''
      self.text = text
      self.display = self.font.render(text, True, WHITE)

   def press(self):
      '''Makes the button appear highlighted.'''
      self.display = self.font.render(self.text, True, GREY)

   def click(self, pos, mouse_down):
      '''Holds the logic for when the button is clicked.
      
         Parameters:
         @pos - Mouse's Coordinates.
         @mouse_down - True if the mouse if being pressed.
      '''
      if pos[0] > self.hitbox[0] and pos[0] < self.hitbox[1] and mouse_down: #clicked in the button
         if pos[1] > self.hitbox[2] and pos[1] < self.hitbox[3]:
            self.pressed = True
            self.display = self.font.render(self.text, True, GREY)
      elif not mouse_down and self.pressed: #mouse lifted after clicking
         self.released = True
         self.pressed = False
      else:
         self.released = False
         self.display = self.font.render(self.text, True, WHITE)
         