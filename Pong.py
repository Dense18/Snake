import pygame
import random
from Food import Food

from colors import *
from Snake import *

class Pong:
    def __init__(self, win, win_width, win_height, block_size, fps = 10):
        self.win = win
        self.win_width = win_width
        self.win_height = win_height
        
        self.block_size = block_size
        self.grid_row = self.win_height // self.block_size
        self.grid_col = self.win_width //self.block_size

        self.snake = Snake(self.grid_col // 2 * self.block_size,self.grid_row// 2 * self.block_size, self.block_size, self.block_size)

        initial_food_x = (random.randint(1, self.win_width//self.block_size) - 1) * self.block_size
        initial_food_y = (random.randint(1, self.win_height//self.block_size) - 1) * self.block_size
        self.food = Food(initial_food_x,initial_food_y,self.block_size, self.block_size)

        self.clock = pygame.time.Clock()
        self.fps = fps

    def run(self):
        running = True

        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_UP]:
                self.snake.set_direction(SNAKE_UP)
            elif key_pressed[pygame.K_DOWN]:
                self.snake.set_direction(SNAKE_DOWN)
            elif key_pressed[pygame.K_LEFT]:
                self.snake.set_direction(SNAKE_LEFT)
            elif key_pressed[pygame.K_RIGHT]:
                self.snake.set_direction(SNAKE_RIGHT)
            
            self.snake.move()

            if (self.handle_collision()):
                self.gameOverScreen()
                pygame.time.delay(2000)
                self.reset()
        
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()

    def draw_grid(self):
        gap_row = self.win_height//self.grid_row
        gap_col = self.win_width//self.grid_col

        for i in range(self.grid_row):
            pygame.draw.line(self.win, GREY, (0, i * gap_row), (self.win_width, i * gap_row))
            for j in range(self.grid_col):
                pygame.draw.line(self.win, GREY, (j * gap_col,0), (j * gap_col, self.win_height))

    def handle_collision(self):
        if self.snake.body[0][0] < 0 or self.snake.body[0][0] + self.snake.width > self.win_width:
            return 1
        if self.snake.body[0][1] < 0 or self.snake.body[0][1] + self.snake.height > self.win_height:
            return 1
        if self.snake.isSelfCollided():
            return 1
        
        if self.snake.body[0] == self.food.pos:
            self.snake.grow()

            ##Prevent food from appearing in any of the snake body
            while(True):
                self.food.randomize(self.win_width, self.win_height)
                if (self.food.pos not in self.snake.body):
                    break;
        return 0

    def draw(self):
        self.win.fill(BLACK)

        self.food.draw(self.win)
        self.snake.draw(self.win)
        self.draw_grid()

        pygame.display.update()

    def reset(self):
        self.snake.reset()
        self.food.randomize(self.win_width, self.win_height)

    def gameOverScreen(self):
        over_text = pygame.font.SysFont("Ariel", 50).render("Game Over", 1, WHITE)

        self.win.fill(BLACK)
        self.win.blit(over_text, (self.win_width //2 - over_text.get_width()//2, self.win_height//2 - over_text.get_height()//2))
        pygame.display.update()
