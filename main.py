import pygame
from random import randint

#Global Variables
black = (0,0,0)
white = (255,255,255)
green = (55, 180, 55)
yellow = (250, 255, 61)
finish = False
clock = pygame.time.Clock()
ground = 774
roof = 26
x_bird = 200
y_bird = 400
x_pipes = 550
y_pipes = 480       #Pipe image has 320 pixels of height.
x_increase = 0
y_increase = 0
pipes_stop = 0
bird_img_sel = 0
background_img = pygame.image.load('media/background-day.png')


#Game display settings
pygame.init()
screen_size = 600, 800
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Flappy Bird')


def bird(x, y, image_sel):
    """  Simple function to bring life to the bird."""
    if image_sel == 0:
        bird_img = pygame.image.load('media/yellowbird-midflap.png')
    elif image_sel == 1:
        bird_img = pygame.image.load('media/yellowbird-upflap.png')
    elif image_sel == 2:
        bird_img = pygame.image.load('media/yellowbird-downflap.png')    
    screen.blit(bird_img, (x, y))    
                
def pipes(x, y):
    """  Simple function to create the obstacles, the pipes."""
    pipe_img_bottom = pygame.image.load('media/pipe-green-bottom.png')
    pipe_img_top = pygame.image.load('media/pipe-green-top.png')
    screen.blit(pipe_img_top, (x, (y-480)))
    screen.blit(pipe_img_bottom, (x, y))
    
    
def gameover():
    """Prints 'game over' when you hit the ground or the roof."""
    font = pygame.font.SysFont(None, 50)
    text = font.render('Game Over Bro!', True, yellow)
    screen.blit(text, [170, 350])
    

#Where everything starts.
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_increase = 4
                bird_img_sel = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_increase = -10  
                bird_img_sel = 1

    screen.blit(background_img, (0,0))        
    
    bird(x_bird, y_bird, bird_img_sel)   
    y_bird += y_increase
    if (y_bird > ground) or (y_bird < roof):
        gameover()
        y_increase = 0
        pipes_stop = 1
    else:
        pipes_stop = 0
    
    pipes(x_pipes, y_pipes)
    if x_pipes == -50 :
        x_pipes = 550
    elif pipes_stop == 0:
        x_pipes -= 3    
        
    pygame.display.flip()
    clock.tick(60)