import pygame
from config import *

class Bar():
   def __init__(self, coords, length, pos):
      self.length = length
      self.pos = pos
      self.coords = coords
      self.pointing = False
      self.held = False
      self.hitbox = [self.coords[0], self.coords[0] + length, self.coords[1], self.coords[1] + 40]
      self.volume = pos

   def render(self, win, dark_theme):
      if dark_theme: 
         bar = pygame.image.load("../assets/images/bar.png")
         if not self.pointing: bar_button = pygame.image.load("../assets/images/bar_button.png")
         else: bar_button = pygame.image.load("../assets/images/bar_button_point.png")
      else: 
         bar = pygame.image.load("../assets/images/bar_light.png")
         if not self.pointing: bar_button = pygame.image.load("../assets/images/bar_button_light.png")
         else: bar_button = pygame.image.load("../assets/images/bar_button_point.png")

      win.blit(bar, self.coords)
      win.blit(bar_button, (self.coords[0] + int(self.pos * self.length), self.coords[1]))

   def allign_right(self, distance, width):
      self.coords[0] = width - distance - self.length
      self.hitbox[0] = self.coords[0]
      self.hitbox[1] = self.hitbox[0] + self.length

   def set_volume(self, volume):
      self.volume = volume

   def drag(self, mouse_pos, mouse_down):
      '''Holds the logic for when the button is dragged.
      
         Parameters:
         @pos - Mouse's Coordinates.
         @mouse_down - True if the mouse if being pressed.
      '''
      pygame.mixer.init()
      button_point = pygame.mixer.Sound("../assets/sounds/button_point.mp3")
      button_point.set_volume(self.volume)
      button_click = pygame.mixer.Sound("../assets/sounds/button_click.mp3")
      button_click.set_volume(self.volume)

      if mouse_pos[0] > self.hitbox[0] and mouse_pos[0] < self.hitbox[1]: #clicked in the button
         if mouse_pos[1] > self.hitbox[2] and mouse_pos[1] < self.hitbox[3]:
            if not self.pointing and not self.held: pygame.mixer.Sound.play(button_point)
            self.pointing = True
         else: self.pointing = False
      else: self.pointing = False

      if self.pointing and mouse_down:
         if not self.held: pygame.mixer.Sound.play(button_click)
         self.held = True
         

      self.held = mouse_down

      if self.held and self.pointing:
         if mouse_pos[0] <= self.coords[0]: self.pos = 0.0
         elif mouse_pos[0] >= self.coords[0] + self.length: self.pos = 1.0
         else: self.pos = (mouse_pos[0] - self.coords[0]) / self.length
