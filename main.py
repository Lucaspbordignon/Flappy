import pygame
import random
from game import *

if __name__ == "__main__":

    test = Game()
    restart = test.play()
    while restart == 1 or restart == 2:
        test = Game()
        if restart == 2:
           restart = test.restart_button()

