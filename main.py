import pygame
import random
from game import *
from gameover import *

if __name__ == "__main__":

    test = Game()
    restart = test.play()
    while restart == 1 or restart == 2:
        test = Game()
        gameover = Gameover()
        if restart == 2:
           restart = gameover.restart_button()

