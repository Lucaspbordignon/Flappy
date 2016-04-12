import pygame
import random
import re

#Global Variables



#Game display settings
pygame.init()
screen_size = 600, 800
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Flappy Bird')


def bird(x, y, image_sel):
    """  Simple function to bring life to the bird."""
    if image_sel == 0:
        bird_img = pygame.image.load('media/images/yellowbird-midflap.png')
    elif image_sel == 1:
        bird_img = pygame.image.load('media/images/yellowbird-upflap.png')
    elif image_sel == 2:
        bird_img = pygame.image.load('media/images/yellowbird-downflap.png')    
    screen.blit(bird_img, (x, y))    
                
def pipes(x, y):
    """  Simple function to create the obstacles, the pipes."""
    pipe_img_bottom = pygame.image.load('media/images/pipe-green-bottom.png')
    pipe_img_top = pygame.image.load('media/images/pipe-green-top.png')
    screen.blit(pipe_img_top, (x, (y-780)))
    screen.blit(pipe_img_bottom, (x, y))
        
    
def gameover():
    """Prints 'game over' when the bird hit the ground or the roof."""
    text = pygame.image.load('media/images/gameover.png')
    screen.blit(text, [200, 350])

def load_score_images(score_img_list):
    """Load external files (images) for the score."""
    score_img_list[0] = pygame.image.load('media/images/0.png')
    score_img_list[1] = pygame.image.load('media/images/1.png')
    score_img_list[2] = pygame.image.load('media/images/2.png')
    score_img_list[3] = pygame.image.load('media/images/3.png')
    score_img_list[4] = pygame.image.load('media/images/4.png')
    score_img_list[5] = pygame.image.load('media/images/5.png')
    score_img_list[6] = pygame.image.load('media/images/6.png')
    score_img_list[7] = pygame.image.load('media/images/7.png')
    score_img_list[8] = pygame.image.load('media/images/8.png')
    score_img_list[9] = pygame.image.load('media/images/9.png')


def score(score_dozen, score_unity, score_img):
    """Show the actual score over the screen."""
    screen.blit(score_img[score_dozen], [290, 100])
    screen.blit(score_img[score_unity], [310, 100])

def restart_game():
    #x_bird, y_bird = 200, 400
    #x_pipes, y_pipes = 550, 480
    #pipes_stop = 0
    #restart = 0
    play()

def restart_button(position):
    if position[0] >= 0 and position[0] <= 100:
        if position[1] >= 0 and position[1] <= 100:
            restart = 1
            
def play():
    #Where everything starts.
    sizes = {'Bird':(34, 24), 'Pipe':(52, 620)}
    score_img = {}
    clock = pygame.time.Clock()
    ground, roof = 774, 1
    x_bird, y_bird = 200, 400
    x_pipes, y_pipes = 550, 480
    y_increase = 0
    pipes_stop = 0
    bird_img_sel = 0
    restart = 0
    score_dozen, score_unity = 0, 0
    mouse_position = (-1, -1)
    background_img = pygame.image.load('media/images/background-day.png')
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()         
            if not pipes_stop == 1: 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        y_increase = 4
                        bird_img_sel = 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_increase = -10  
                        bird_img_sel = 1
       

        #Initialize the bird and the background.
        screen.blit(background_img, (0,0))              
        bird(x_bird, y_bird, bird_img_sel)   
        y_bird += y_increase
        load_score_images(score_img)

        #Moves the pipes.
        pipes(x_pipes, y_pipes)
        if x_pipes == -50 :
            x_pipes = 550
            y_pipes = random.randint(210, 750)
        elif pipes_stop == 0:
            x_pipes -= 3 
       
        restart_button(mouse_position)
        #Count the score.
        if x_bird > x_pipes+48 and x_bird < x_pipes+52:
            if score_unity == 9:
                score_dozen += 1
                score_unity = 0
            else :  
                score_unity += 1
        score(score_dozen, score_unity, score_img)

        if restart == 1:
            restart_game()
        elif (y_bird > ground) or (y_bird < roof):
            # Bird dies
            gameover()
            restart_game()
            y_increase = 0
            pipes_stop = 1
        elif ((x_bird + sizes['Bird'][0])>=x_pipes)and(x_bird<=(x_pipes+50)):
            if ((y_bird + sizes['Bird'][1])>=y_pipes)or(y_bird<=(y_pipes-160)):
                # Bird dies
                gameover()
                restart_game()
                y_increase = 0
                pipes_stop = 1
        else:
            pipes_stop = 0

        #Update the screen.    
        pygame.display.flip()
        clock.tick(60)

play()
