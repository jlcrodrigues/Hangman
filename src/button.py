import pygame
from config import *

class Button:
   def __init__(self, text, coords, letter_size):
      self.font = pygame.font.Font(FONT_NAME, letter_size)
      self.text = text    
      self.display = self.font.render(text, True, WHITE)
      self.coords = coords
      self.clicked = False
      self.pressed = False
      self.held = True
      self.width = self.display.get_width()
      self.hitbox = [coords[0], coords[0] + self.display.get_width(), coords[1], coords[1] + self.display.get_height()]

   def render(self, win):
      '''Renders the button on the screen.'''
      win.blit(self.display, self.coords)

   def center(self):
      '''Centers the button horizontally.'''
      self.coords[0] = SCREEN_WIDTH / 2 - self.width / 2
      self.hitbox[0] = self.coords[0]
      self.hitbox[1] = self.hitbox[0] + self.width

   def set_x(self, x):
      '''Changes the x coordinate of the button.'''
      self.coords[0] = x
      self.hitbox[0] = x
      self.hitbox[1] = x + self.display.get_width()

   def set_text(self, text):
      '''Changes the button's text.'''
      #self.text = text
      self.display = self.font.render(text, True, WHITE)
      if self.pressed: self.display = self.font.render(text, True, GREY)

   def press(self):
      '''Makes the button appear highlighted.'''
      self.display = self.font.render(self.text, True, GREY)
      self.pressed = True

   def unpress(self):
      '''Makes the button not appear highlighted.'''
      self.display = self.font.render(self.text, True, WHITE)
      self.pressed = False
      #self.clicked = False

   def click(self, pos, mouse_down):
      '''Holds the logic for when the button is clicked.
      
         Parameters:
         @pos - Mouse's Coordinates.
         @mouse_down - True if the mouse if being pressed.
      '''
      if pos[0] > self.hitbox[0] and pos[0] < self.hitbox[1] and not self.held: #clicked in the button
         if pos[1] > self.hitbox[2] and pos[1] < self.hitbox[3]:
            self.press()
            if mouse_down: 
               self.clicked = True
               self.held = True
         else:
            self.unpress()
      else:
         self.unpress()
         self.clicked = False
      if not mouse_down: 
         self.clicked = False
         self.held = False
      
         