import pygame
import random


class Game:

    def __init__(self):
        pygame.init()
        self.screen_size = (400, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Flappy Bird')

        self.img_sizes = {'Bird': (34, 24), 'Pipe': (52, 620)}
        self.score_img = {}
        self.clock = pygame.time.Clock()
        self.ground = self.screen_size[1]-self.img_sizes['Bird'][1]
        self.roof = 0

        self.space_between_pipes = 110  # Space between top and bottom pipes
        self.pipe_limits = 50  # Boundary to blit pipes
        # Upper and lower bound limits to pass to randint
        self.rand_low = self.space_between_pipes + self.pipe_limits
        self.rand_high = self.screen_size[1] - self.pipe_limits

        self.x_bird = self.screen_size[0]/3.0
        self.y_bird = self.screen_size[1]/2.5

        self.x_pipe = self.screen_size[0]*(5.0/6.0)
        self.y_pipe = random.randint(self.rand_low, self.rand_high)

        self.x_second_pipe = self.x_pipe + \
            (self.screen_size[0] + self.img_sizes['Pipe'][0])/2.0
        self.y_second_pipe = random.randint(self.rand_low, self.rand_high)

        self.y_increase = 0.0
        self.pipes_stop = False
        self.score_val = 0
        self.mouse_position = (0, 0)

        self.background_img = \
            pygame.image.load('media/images/background-day.png')
        self.pipe_img_bottom = \
            pygame.image.load('media/images/pipe-green-bottom.png')
        self.pipe_img_top = \
            pygame.image.load('media/images/pipe-green-top.png')

        self.gameover_img = pygame.image.load('media/images/gameover.png')
        self.restart_button_img = \
            pygame.image.load('media/images/restart-button.png')

        # Where restart button will be blitted
        self.restart_button_xy = \
            ((self.screen_size[0]-130)/2.0, (self.screen_size[1])*(3.0/4.0))

        # Variables used in detect_score() method
        self.passed1 = False
        self.passed2 = False

    def bird(self):
        """Simple function to bring life to the bird."""
        if self.y_increase == 0:
            self.bird_img = \
                pygame.image.load('media/images/yellowbird-midflap.png')
        elif self.y_increase < 0:
            self.bird_img = \
                pygame.image.load('media/images/yellowbird-upflap.png')
        elif self.y_increase > 0:
            self.bird_img = \
                pygame.image.load('media/images/yellowbird-downflap.png')
        self.screen.blit(self.bird_img, (self.x_bird, self.y_bird))

    def pipes(self):
        """Simple function to update the pipes positions."""

        pipes_speed = 2

        if self.x_pipe <= -self.img_sizes['Pipe'][0]:
            self.x_pipe = self.screen_size[0]
            self.y_pipe = random.randint(self.rand_low, self.rand_high)
        if self.x_second_pipe <= -self.img_sizes['Pipe'][0]:
            self.x_second_pipe = self.screen_size[0]
            self.y_second_pipe = random.randint(self.rand_low, self.rand_high)
        elif not self.pipes_stop:
            self.x_second_pipe -= pipes_speed
            self.x_pipe -= pipes_speed

        self.blit_pipes()

    def blit_pipes(self):
        """Blits the pipes to their current position."""

        # Blit first pipe
        y_top = self.y_pipe-(self.img_sizes['Pipe'][1]+self.space_between_pipes)
        self.screen.blit(self.pipe_img_top, (self.x_pipe, y_top))
        self.screen.blit(self.pipe_img_bottom, (self.x_pipe, self.y_pipe))

        # Blit second pipe
        y_top = self.y_second_pipe - \
            (self.img_sizes['Pipe'][1]+self.space_between_pipes)
        self.screen.blit(self.pipe_img_top, (self.x_second_pipe, y_top))
        self.screen.blit(self.pipe_img_bottom,
            (self.x_second_pipe, self.y_second_pipe))

    def gameover(self):
        """Prints 'game over' when the bird hit the ground or the roof."""

        # Blits game over in the middle of the screen
        self.screen.blit(self.gameover_img,
            [(self.screen_size[0]-192)/2.0, (self.screen_size[1]-42)/2.0])
        # Blits restart button to the half bottom of the screen
        self.screen.blit(self.restart_button_img, self.restart_button_xy)

    def restart_button(self):
        """Wait for a mouse click to reset or finish the game."""

        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_position = pygame.mouse.get_pos()
            if self.restart_button_xy[0] <= self.mouse_position[0] <= \
                    self.restart_button_xy[0] + 130:
                if self.restart_button_xy[1] <= self.mouse_position[1] <= \
                       self.restart_button_xy[1] + 40:
                    return self.play()
                    break

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

    def detect_score(self):
        """
        Detects if bird passed one of the pipes and adds to the score if so
        """

        # Detect first pipe
        if (self.x_bird > self.x_pipe + self.img_sizes['Pipe'][0]) \
                and not self.passed1:
            self.score_val += 1
            self.passed1 = True
        if (self.x_pipe + self.img_sizes['Pipe'][0] > self.x_bird) \
                and self.passed1:
            self.passed1 = False

        # Detect second pipe
        if (self.x_bird > self.x_second_pipe + self.img_sizes['Pipe'][0]) \
                and not self.passed2:
            self.score_val += 1
            self.passed2 = True
        if (self.x_second_pipe + self.img_sizes['Pipe'][0] > self.x_bird) \
                and self.passed2:
            self.passed2 = False

    def score(self):
        """Show the actual score over the screen."""
        self.detect_score()
        if (self.score_val < 10):
            self.screen.blit(self.score_img[self.score_val],
                [self.screen_size[0]/2 - 10, 100])
        else:
            str_score_val = str(self.score_val)
            self.screen.blit(self.score_img[int(str_score_val[0])],
                [self.screen_size[0]/2 - 22, 100])
            self.screen.blit(self.score_img[int(str_score_val[1])],
                [self.screen_size[0]/2, 100])

    def bird_dies(self):
        """returns True if bird is dead"""

        if (self.y_bird + 5 > self.ground) or (self.y_bird < self.roof):
            # Bird dies
            return True

        elif ((self.x_bird + self.img_sizes['Bird'][0]) >= self.x_pipe) and \
                (self.x_bird <= (self.x_pipe+self.img_sizes['Pipe'][0])):
            if ((self.y_bird + self.img_sizes['Bird'][1]) >= self.y_pipe) or \
                   (self.y_bird <= (self.y_pipe-self.space_between_pipes)):
                # Bird dies
                return True
        elif ((self.x_bird+self.img_sizes['Bird'][0]) >= self.x_second_pipe)\
                and(self.x_bird <= (self.x_second_pipe+self.img_sizes['Pipe'][0])):
            if ((self.y_bird+self.img_sizes['Bird'][1]) >= self.y_second_pipe)\
                    or(self.y_bird <= (self.y_second_pipe -
                                            self.space_between_pipes)):
                # Bird dies
                return True

    def play(self):
        """Initialize the software."""
        self.load_score_images()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if not self.pipes_stop:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.y_increase = -5

            # Initialize the bird and the background.
            self.screen.blit(self.background_img, (0, 0))

            self.y_increase += 0.25  # Simulates gravity acceleration

            self.pipes()  # Update pipes

            # Count the score.
            self.score()

            if self.bird_dies():
                # Bird dies
                self.bird()
                self.gameover()
                pygame.display.flip()
                return 1
                self.y_increase = 0
                self.pipes_stop = True
            else:
                self.pipes_stop = False

            self.bird()
            self.y_bird += self.y_increase

            # Update the screen.
            pygame.display.flip()
            self.clock.tick(60)
