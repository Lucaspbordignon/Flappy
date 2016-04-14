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
        self.ground, self.roof = 774, 1
        self.x_bird, self.y_bird = 200, 400
        self.x_pipe, self.y_pipe = 550, random.randint(210, 750)  
        self.x_second_pipe, self.y_second_pipe = 900, random.randint(210, 750)  
        self.bird_img_sel = 0
        self.y_increase = 0
        self.pipes_stop = 0
        self.score_dozen, self.score_unity = 0, 0
        self.mouse_position = (0, 0)
        self.background_img=pygame.image.load('media/images/background-day.png')
        self.pipe_img_bottom = pygame.image.load('media/images/pipe-green-bottom.png')
        self.pipe_img_top = pygame.image.load('media/images/pipe-green-top.png')
    
    def bird(self, x, y, image_sel):
        """Simple function to bring life to the bird."""
        if image_sel == 0:
            self.bird_img = pygame.image.load('media/images/yellowbird-midflap.png')
        elif image_sel == 1:
            self.bird_img = pygame.image.load('media/images/yellowbird-upflap.png')
        elif image_sel == 2:
            self.bird_img = pygame.image.load('media/images/yellowbird-downflap.png')    
        self.screen.blit(self.bird_img, (x, y))

    def pipes(self, x, y):
        """Simple function to create and move the obstacles, the pipes."""
        self.screen.blit(self.pipe_img_top, (x, (y-780)))
        self.screen.blit(self.pipe_img_bottom, (x, y))
        if self.x_pipe == -50:
            self.x_pipe = 700
            self.y_pipe = random.randint(210, 750)
        if self.x_second_pipe == -50:
            self.x_second_pipe = 700
            self.y_second_pipe = random.randint(210, 750)    
        elif self.pipes_stop == 0:
            self.x_second_pipe -= 2 
            self.x_pipe -= 2
    def gameover(self):
        """Prints 'game over' when the bird hit the ground or the roof."""
        self.text = pygame.image.load('media/images/gameover.png')
        self.restart_button_img = pygame.image.load('media/images/restart-button.png')
        self.screen.blit(self.text, [200, 350])
        self.screen.blit(self.restart_button_img, [235, 550])
            
    def restart_button(self):
        """Wait for a mouse click to reset or finish the game."""
        while self.mouse_position == (0,0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_position = pygame.mouse.get_pos()

        if 235 <= self.mouse_position[0] <= 365:
            if 550 <= self.mouse_position[1] <= 590:
                self.mouse_position = (0, 0)
                return self.play()             
            
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

    def score(self):
        """Show the actual score over the screen."""
        self.screen.blit(self.score_img[self.score_dozen], [290, 100])
        self.screen.blit(self.score_img[self.score_unity], [310, 100])
    
    def play(self):
        """Initialize the software."""
        self.load_score_images()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_position = pygame.mouse.get_pos()         
                if not self.pipes_stop == 1: 
                    if event.type == pygame.KEYUP:
                        self.y_increase = 7
                        self.bird_img_sel = 2
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.y_increase = -5  
                            self.bird_img_sel = 1 
                    
            #Initialize the bird and the background.
            self.screen.blit(self.background_img, (0,0))              
            self.bird(self.x_bird,self. y_bird, self.bird_img_sel)   
            self.y_bird += self.y_increase
            
            #Moves the pipes.
            self.pipes(self.x_pipe, self.y_pipe)
            self.pipes(self.x_second_pipe, self.y_second_pipe)
                       
            #Count the score.
            if self.x_bird > self.x_pipe+48 and self.x_bird < self.x_pipe+52:
                if self.score_unity == 9:
                    self.score_dozen += 1
                    self.score_unity = 0
                else :  
                    self.score_unity += 1
            self.score()

            if (self.y_bird > self.ground+4) or (self.y_bird < self.roof-4):
                # Bird dies
                self.gameover()
                pygame.display.flip()
                return 2 
                self.y_increase = 0
                self.pipes_stop = 1
            elif ((self.x_bird + self.sizes['Bird'][0])>=self.x_pipe+3)and(self.x_bird<=(self.x_pipe+50)):
                if ((self.y_bird + self.sizes['Bird'][1])>=self.y_pipe)or(self.y_bird<=(self.y_pipe-160)):
                    # Bird dies
                    self.gameover()
                    pygame.display.flip()
                    return 2 
                    self.y_increase = 0
                    self.pipes_stop = 1
            elif ((self.x_bird + self.sizes['Bird'][0])>=self.x_second_pipe+3)and(self.x_bird<=(self.x_second_pipe+50)):
                if ((self.y_bird + self.sizes['Bird'][1])>=self.y_second_pipe)or(self.y_bird<=(self.y_second_pipe-160)):
                    self.gameover()
                    pygame.display.flip()
                    return 2
                    self.y_increase = 0
                    self.pipes_stop = 1
            else:
                self.pipes_stop = 0

            #Update the screen.    
            pygame.display.flip()
            self.clock.tick(60)
