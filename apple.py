import pygame


class Apple:
    def __init__(self, location):
        self.location = location

    def render(self, screen):
        pygame.draw.circle(screen, (200, 0, 0), self.location, 5)
