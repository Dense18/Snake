from colors import *
import pygame

SNAKE_UP = 1
SNAKE_DOWN = 2
SNAKE_LEFT = 3
SNAKE_RIGHT = 4

class Snake:
    def __init__(self, x,y, width, height , body_color = GREEN, head_color = ORANGE):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.body_color = body_color
        self.head_color = head_color
        self.eye_color = PURPLE
        self.length = self.original_length = 1

        self.dir = SNAKE_UP
        self.body = [[x,y]]
    
    def draw(self, win):
        ## Head
        pygame.draw.rect(win, self.head_color, (self.body[0][0], self.body[0][1], self.width, self.height))
        ## Eyes for the head
        left_eyes_pos = self.body[0][0] + self.width * 1/4, self.body[0][1] + self.height * 1/4
        right_eyes_pos = self.body[0][0] + self.width * 3/4, self.body[0][1] + self.height * 1/4
        radius = self.height * 1/4

        pygame.draw.circle(win, self.eye_color, left_eyes_pos, radius)
        pygame.draw.circle(win, self.eye_color, right_eyes_pos, radius)

        ##Body
        for i in range (1, self.length):
            pygame.draw.rect(win, self.body_color, (self.body[i][0], self.body[i][1], self.width, self.height))
    
    def set_direction(self, dir):
        self.dir = dir

    def move(self):
        ##Update body
        for i in range(self.length-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

        ## Update head
        if self.dir == SNAKE_UP:
            self.body[0][1] -= 1  * self.height
        elif self.dir == SNAKE_DOWN:
            self.body[0][1] += 1 * self.height
        elif self.dir == SNAKE_LEFT:
            self.body[0][0] -= 1 * self.width
        elif self.dir == SNAKE_RIGHT:
            self.body[0][0] += 1 * self.width

    def grow(self):

        tail = self.body[len(self.body) - 1][0], self.body[len(self.body) - 1][1] ##x, y
        if (self.length == 1):
            if (self.dir == SNAKE_DOWN):
                self.body.append([ tail[0], tail[1] - self.height ] )
            elif self.dir == SNAKE_UP:
                self.body.append([ tail[0], tail[1] + self.height ] )
            elif self.dir == SNAKE_RIGHT:
                self.body.append([ tail[0] - self.width, tail[1] ] )
            elif self.dir == SNAKE_LEFT:
                self.body.append([ tail[0] + self.width, tail[1] ] )
        
        else:
            tail2 = self.body[len(self.body) - 2][0], self.body[len(self.body) - 2][1]
            if (tail2[1] > tail[1] and tail[0] == tail2[0]): ##DOWN
                self.body.append([ tail[0], tail[1] - self.height ] )
            elif (tail[1] > tail2[1] and tail[0] == tail2[0]): ## UP
                self.body.append([ tail[0], tail[1] + self.height ] )
            elif (tail2[0] > tail[0] and tail[1] == tail2[1]): ##RIGHT
                self.body.append([ tail[0] - self.width, tail[1] ] )
            elif (tail[0] > tail2[0] and tail[1] == tail2[1]): ##LEFT
                self.body.append([ tail[0] + self.width, tail[1] ] )
        
        self.length += 1

        # if (self.dir == SNAKE_DOWN):
        #     self.body.append([ tail[0], tail[1] - self.height ] )
        # elif self.dir == SNAKE_UP:
        #     self.body.append([ tail[0], tail[1] + self.height ] )
        # elif self.dir == SNAKE_RIGHT:
        #     self.body.append([ tail[0] - self.width, tail[1] ] )
        # elif self.dir == SNAKE_LEFT:
        #     self.body.append([ tail[0] + self.width, tail[1] ] )

    def isSelfCollided(self):
        for i in range(1, self.length):
            if self.body[0] == self.body[i]:
                return True
        
        return False

    def reset(self):
        self.length = self.original_length
        self.x = self.original_x
        self.y = self.original_y
        self.body = [[self.x, self.y]]
    
