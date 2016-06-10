from game import *

if __name__ == "__main__":

    game = Game()
    restart = game.play()
    while restart == 1:
        game = Game()
        restart = game.restart_button()
