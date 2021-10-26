import pygame
from config import *

class Button:
   def __init__(self, text, coords, letter_size, is_image = False):
      self.font = pygame.font.Font(FONT_NAME, letter_size)
      self.text = text    
      self.display = self.font.render(text, True, WHITE)
      if is_image: self.display = pygame.image.load(text)
      self.is_image = is_image
      self.coords = coords
      self.pointing = False #True if the mouse is over the button
      self.held = False #True if the mouse is clicking the button
      self.clicked = False #True if the mouse has been clicked
      self.width = self.display.get_width()
      self.volume = 1.0
      self.hitbox = [coords[0], coords[0] + self.display.get_width(), coords[1], coords[1] + self.display.get_height()]

   def render(self, win):
      '''Renders the button on the screen.'''
      win.blit(self.display, self.coords)

   def center(self, width):
      '''Centers the button horizontally.'''
      self.coords[0] = width / 2 - self.width / 2
      self.hitbox[0] = self.coords[0]
      self.hitbox[1] = self.hitbox[0] + self.width

   def allign_right(self, distance, width):
      self.coords[0] = width - distance - self.width
      self.hitbox[0] = self.coords[0]
      self.hitbox[1] = self.hitbox[0] + self.width

   def set_x(self, x):
      '''Changes the x coordinate of the button.'''
      self.coords[0] = x
      self.hitbox[0] = x
      self.hitbox[1] = x + self.display.get_width()

   def set_y(self, y):
      '''Changes the y coordinate of the button.'''
      self.coords[1] = y
      self.hitbox[2] = y
      self.hitbox[3] = y + self.display.get_width()


   def set_text(self, text, dark_theme):
      '''Changes the button's text.'''
      if not self.is_image:
         if self.pointing: self.display = self.font.render(text, True, GREY)
         elif self.held: self.display = self.font.render(text, True, RED)
         else: 
            if dark_theme: self.display = self.font.render(text, True, WHITE)
            else: self.display = self.font.render(text, True, BLACK)

      else:
         if self.pointing: self.display = pygame.image.load(text[:-4] + "_pressed.png")
         elif dark_theme: self.display = pygame.image.load(text)
         else: self.display = pygame.image.load(text[:-4] + "_light.png")

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

   def set_volume(self, volume):
      self.volume = volume

   def click(self, pos, mouse_down):
      '''Holds the logic for when the button is clicked.
      
         Parameters:
         @pos - Mouse's Coordinates.
         @mouse_down - True if the mouse if being pressed.
      '''
      pygame.mixer.init()
      button_point = pygame.mixer.Sound("../assets/sounds/button_point.mp3")
      button_point.set_volume(self.volume)
      button_click = pygame.mixer.Sound("../assets/sounds/button_click.mp3")
      button_click.set_volume(self.volume)

      if pos[0] > self.hitbox[0] and pos[0] < self.hitbox[1]: #clicked in the button
         if pos[1] > self.hitbox[2] and pos[1] < self.hitbox[3]:
            if not self.pointing: pygame.mixer.Sound.play(button_point)
            self.pointing = True
         else: self.pointing = False
      else: self.pointing = False

      if self.pointing:
         if self.held and not mouse_down:
            self.clicked = True
            pygame.mixer.Sound.play(button_click)
         self.held = mouse_down

      #if self.text == 'play': print(self.held)
      #self.update()
      