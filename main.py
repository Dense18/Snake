import pygame
import random
from Food import Food

from settings import *
from colors import *
from Snake import *

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


## Fonts
SCORE_FONT = pygame.font.SysFont("Ariel", 50)

BLOCK_SIZE = 20

GRID_ROW = HEIGHT // BLOCK_SIZE
GRID_COL = WIDTH // BLOCK_SIZE


def main():
    running = True
    snake = Snake(GRID_COL // 2 * BLOCK_SIZE,GRID_ROW // 2 * BLOCK_SIZE,BLOCK_SIZE, BLOCK_SIZE)

    initial_food_x = (random.randint(1, WIDTH//BLOCK_SIZE) - 1) * BLOCK_SIZE
    initial_food_y = (random.randint(1, HEIGHT//BLOCK_SIZE) - 1) * BLOCK_SIZE
    food = Food(initial_food_x,initial_food_y,BLOCK_SIZE, BLOCK_SIZE)

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            snake.set_direction(SNAKE_UP)
        elif key_pressed[pygame.K_DOWN]:
            snake.set_direction(SNAKE_DOWN)
        elif key_pressed[pygame.K_LEFT]:
            snake.set_direction(SNAKE_LEFT)
        elif key_pressed[pygame.K_RIGHT]:
            snake.set_direction(SNAKE_RIGHT)
        
        snake.move()

        if (handle_collision(snake, food)):
            gameOverScreen(WIN)
            pygame.time.delay(2000)
            reset(snake, food)

    
        draw(WIN, snake, food)
        clock.tick(FPS)

    pygame.quit()

def draw_grid(win, row, col, width, height):
    gap_row = height//row
    gap_col = width//col

    for i in range(row):
        pygame.draw.line(win, GREY, (0, i * gap_row), (width, i * gap_row))
        for j in range(col):
            pygame.draw.line(win, GREY, (j * gap_col,0), (j * gap_col, height))

def handle_collision(snake, food):
    if snake.body[0][0] < 0 or snake.body[0][0] + snake.width > WIDTH:
        return 1
    if snake.body[0][1] < 0 or snake.body[0][1] + snake.height > HEIGHT:
        return 1
    if snake.isSelfCollided():
        return 1
    
    if snake.body[0] == food.pos:
        snake.grow()
        food.randomize(WIDTH, HEIGHT)
    
    return 0

def draw(win, snake, food):
    win.fill(BLACK)

    food.draw(win)
    snake.draw(win)
    draw_grid(win, GRID_ROW,GRID_COL, WIDTH, HEIGHT)

    pygame.display.update()

def reset(snake, food):
    snake.reset()
    food.randomize(WIDTH, HEIGHT)

def gameOverScreen(win):
    over_text = SCORE_FONT.render("Game Over", 1, WHITE)

    win.fill(BLACK)
    win.blit(over_text, (WIDTH //2 - over_text.get_width()//2, HEIGHT//2 - over_text.get_height()//2))
    pygame.display.update()

if __name__ == "__main__":
    main()
