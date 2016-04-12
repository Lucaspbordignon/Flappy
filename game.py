import pygame
import random

class Game:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.sizes = {'Bird':(34, 24), 'Pipe':(52, 620)}
        self.score_img = {}
        self.clock = pygame.time.Clock()
        self.ground = 774
        self.roof = 1
        self.x_bird = 200
        self.y_bird = 400
        self.x_pipes = 550
        self.y_pipes = 480
        self.y_increase = 0
        self.pipes_stop = 0
        self.bird_img_sel = 0
        self.restart = 0
        self.score_dozen = 0
        self.score_unity = 0
        self.mouse_position = (-1, -1)
        self.background_img=pygame.image.load('media/images/background-day.png')
    
    def bird(self, x, y, image_sel):
        """  Simple function to bring life to the bird."""
        if image_sel == 0:
            self.bird_img = pygame.image.load('media/images/yellowbird-midflap.png')
        elif image_sel == 1:
            self.bird_img = pygame.image.load('media/images/yellowbird-upflap.png')
        elif image_sel == 2:
            self.bird_img = pygame.image.load('media/images/yellowbird-downflap.png')    
        self.screen.blit(self.bird_img, (x, y))

    def pipes(self, x, y):
        """  Simple function to create the obstacles, the pipes."""
        self.pipe_img_bottom = pygame.image.load('media/images/pipe-green-bottom.png')
        self.pipe_img_top = pygame.image.load('media/images/pipe-green-top.png')
        self.screen.blit(self.pipe_img_top, (x, (y-780)))
        self.screen.blit(self.pipe_img_bottom, (x, y))
    
    def gameover(self):
        """Prints 'game over' when the bird hit the ground or the roof."""
        text = pygame.image.load('media/images/gameover.png')
        self.screen.blit(text, [200, 350])
    
    def load_score_images(self):
        """Load external files (images) for the score."""
        self.score_img[0] = pygame.image.load('media/images/0.png')
        self.score_img[1] = pygame.image.load('media/images/1.png')
        self.score_img[2] = pygame.image.load('media/images/2.png')
        self.score_img[3] = pygame.image.load('media/images/3.png')
        self.score_img[4] = pygame.image.load('media/images/4.png')
        self.score_img[5] = pygame.image.load('media/images/5.png')
        self.score_img[6] = pygame.image.load('media/images/6.png')
        self.score_img[7] = pygame.image.load('media/images/7.png')
        self.score_img[8] = pygame.image.load('media/images/8.png')
        self.score_img[9] = pygame.image.load('media/images/9.png')

    def score(self, score_dozen, score_unity):
        """Show the actual score over the screen."""
        self.screen.blit(self.score_img[score_dozen], [290, 100])
        self.screen.blit(self.score_img[score_unity], [310, 100])
    
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_position = pygame.mouse.get_pos()         
                if not self.pipes_stop == 1: 
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            self.y_increase = 4
                            self.bird_img_sel = 2
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.y_increase = -10  
                            self.bird_img_sel = 1
           

            #Initialize the bird and the background.
            self.screen.blit(self.background_img, (0,0))              
            self.bird(self.x_bird,self. y_bird, self.bird_img_sel)   
            self.y_bird += self.y_increase
            self.load_score_images()

            #Moves the pipes.
            self.pipes(self.x_pipes, self.y_pipes)
            if self.x_pipes == -50 :
                self.x_pipes = 550
                self.y_pipes = random.randint(210, 750)
            elif self.pipes_stop == 0:
                self.x_pipes -= 3 
           
            #Count the score.
            if self.x_bird > self.x_pipes+48 and self.x_bird < self.x_pipes+52:
                if self.score_unity == 9:
                    self.score_dozen += 1
                    self.score_unity = 0
                else :  
                    self.score_unity += 1
            self.score(self.score_dozen, self.score_unity)

            if (self.y_bird > self.ground) or (self.y_bird < self.roof):
                # Bird dies
                self.gameover()
                return 1
                self.y_increase = 0
                self.pipes_stop = 1
            elif ((self.x_bird + self.sizes['Bird'][0])>=self.x_pipes)and(self.x_bird<=(self.x_pipes+50)):
                if ((self.y_bird + self.sizes['Bird'][1])>=self.y_pipes)or(self.y_bird<=(self.y_pipes-160)):
                    # Bird dies
                    self.gameover()
                    return 1
                    self.y_increase = 0
                    self.pipes_stop = 1
            else:
                self.pipes_stop = 0

            #Update the screen.    
            pygame.display.flip()
            self.clock.tick(60)

