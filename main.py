import pygame
from Game import *
from settings import *

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

BLOCK_SIZE = 20

GRID_ROW = HEIGHT // BLOCK_SIZE
GRID_COL = WIDTH // BLOCK_SIZE

def main():
    game = Game(WIN, WIDTH, HEIGHT, BLOCK_SIZE)
    game.run()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
