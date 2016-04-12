import pygame
import random
from game import *

if __name__ == "__main__":
    test = Game()
    restart = test.play()
    while restart == 1:
        test = Game()
        restart = test.play()

