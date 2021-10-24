import pygame
from config import *

class Button:
   def __init__(self, text, coords, letter_size):
      self.font = pygame.font.Font(FONT_NAME, letter_size)
      self.text = text    
      self.display = self.font.render(text, True, WHITE)
      self.coords = coords
      self.pointing = False #True if the mouse is over the button
      self.held = False #True if the mouse is clicking the button
      self.clicked = False #True if the mouse has been clicked
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

   def allign_right(self, distance):
      self.coords[0] = SCREEN_WIDTH - distance - self.width
      self.hitbox[0] = self.coords[0]
      self.hitbox[1] = self.hitbox[0] + self.width

   def set_x(self, x):
      '''Changes the x coordinate of the button.'''
      self.coords[0] = x
      self.hitbox[0] = x
      self.hitbox[1] = x + self.display.get_width()

   def set_text(self, text, dark_theme):
      '''Changes the button's text.'''
      if self.pointing: self.display = self.font.render(text, True, GREY)
      elif self.held: self.display = self.font.render(text, True, RED)
      else: 
         if dark_theme: self.display = self.font.render(text, True, WHITE)
         else: self.display = self.font.render(text, True, BLACK)

   def update(self):
      '''Makes the button appear highlighted.'''
      if self.pointing: self.display = self.font.render(self.text, True, GREY)
      elif self.held: self.display = self.font.render(self.text, True, RED)
      else: self.display = self.font.render(self.text, True, WHITE)

   def press(self):
      '''Makes the button not appear highlighted.'''
      self.pointing = True
      self.update()
      #self.clicked = False

   def check(self):
      if self.clicked:
         self.clicked = False
         return True
      return False

   def click(self, pos, mouse_down):
      '''Holds the logic for when the button is clicked.
      
         Parameters:
         @pos - Mouse's Coordinates.
         @mouse_down - True if the mouse if being pressed.
      '''
      if pos[0] > self.hitbox[0] and pos[0] < self.hitbox[1]: #clicked in the button
         if pos[1] > self.hitbox[2] and pos[1] < self.hitbox[3]:
            self.pointing = True
         else: self.pointing = False
      else: self.pointing = False

      if self.pointing:
         if self.held and not mouse_down: self.clicked = True
         self.held = mouse_down

      #if self.text == 'play': print(self.held)
      #self.update()
      