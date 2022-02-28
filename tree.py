import pygame
from pygame.math import Vector2
import random


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

    def render(self, screen):
        pygame.draw.line(screen, (100, 100, 20), self.start, self.end_pos)
        [branch.render(screen) for branch in self.branches]

    def branch(self):
        if self.branches:
            random.choice(self.branches).branch()
            return
        new_direction_l = self.direction.rotate(- self.ROTATE)
        new_direction_r = self.direction.rotate(self.ROTATE)
        self.branches.append(Tree(self.end_pos, new_direction_l, self.length * self.SMALLER))
        self.branches.append(Tree(self.end_pos, new_direction_r, self.length * self.SMALLER))
