import pygame 
from pygame.math import Vector2
import random
from apple import Apple


class Tree:
    ROTATE = 30
    SMALLER = 0.9

    def __init__(self, start, direction, length):
        self.start = start
        self.direction = Vector2(direction)
        self.length = length
        self.branches = []
        self.end_pos = (self.start[0] + self.direction.x * self.length, 
                        self.start[1] + self.direction.y * self.length)
        self.apple = None

    def render(self, screen):
        thickness = int(self.length / 15)
        pygame.draw.line(screen, (100, 100, 20), self.start, self.end_pos, thickness)
        [branch.render(screen) for branch in self.branches]
        if self.apple:
            self.apple.render(screen)

    def branch(self):
        new_direction_l = self.direction.rotate(- self.ROTATE)
        new_direction_r = self.direction.rotate(self.ROTATE)
        self.branches.append(Tree(self.end_pos, new_direction_l, self.length * self.SMALLER))
        self.branches.append(Tree(self.end_pos, new_direction_r, self.length * self.SMALLER))
        self.apple = None

    def grow(self):
        if self.branches:
            return random.choice(self.branches).grow()
        self.apple = Apple(self.end_pos, self)
        return self.apple


