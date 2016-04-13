import pygame
from game import *

class Gameover:
    def __init__(self):
        self.mouse_position = (0, 0)
        self.game = Game()
    
    def restart_button(self):
        while self.mouse_position == (0,0):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_position = pygame.mouse.get_pos()

        if 235 <= self.mouse_position[0] <= 365:
            if 550 <= self.mouse_position[1] <= 590:
                self.mouse_position = (0, 0)
                return self.game.play()       