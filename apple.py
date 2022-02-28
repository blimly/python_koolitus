import pygame


class Apple:
    def __init__(self, location, tree):
        self.location = location
        self.x, self.y = location[0] // 20 * 20, location[1] // 20 * 20
        self.tree = tree

    def render(self, screen):
        pygame.draw.circle(screen, (200, 0, 0), self.location, 5)
