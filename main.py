import pygame
from random import randint

#Global Variables
black = (0,0,0)
white = (255,255,255)
green = (55, 180, 55)
finish = False
clock = pygame.time.Clock()
ground = 774
roof = 26
x_bird = 200
y_bird = 400
x_increase = 0
y_increase = 0
x_location = 600
y_location = 0
x_size = 70
y_size = randint(0, 350)
space = 120
background_img = pygame.image.load('background-day.png')

#Game display settings
pygame.init()
screen_size = 600, 800
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Flappy Bird')


def bird(x, y):
    """  Simple function to bring life to the bird."""
    pygame.draw.circle(screen, black, [x, y], 26)

def pipes(x_location, y_location, x_size, y_size):
    """  Simple function to create the obstacles, the pipes."""
    pygame.draw.rect(screen, green, [x_location, y_location, x_size, y_size])
    
def gameover():
    """Prints 'game over' when you hit the ground or the roof."""
    font = pygame.font.SysFont(None, 40)
    text = font.render('Game Over Bro!', True, green)
    screen.blit(text, [200, 400])
    

#Where everything starts.
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_increase = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_increase = -12  
    
    screen.fill(white)
    screen.blit(background_img, (0,0))    
    
    bird(x_bird, y_bird)
    y_bird += y_increase
    if (y_bird > ground) or (y_bird < roof):
        gameover()
        y_increase = 0
    
    pygame.display.flip()
    clock.tick(60)