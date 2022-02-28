import pygame


class Snake:
    def __init__(self, start_x, start_y):
        self.size = 20
        self.location = [(start_x - self.size * i, start_y) for i in range(5)]
        self.dir = (1, 0)

    def update(self):
        next_loc = (self.location[0][0] + self.dir[0] * self.size, self.location[0][1] + self.dir[1] * self.size)
        self.location.insert(0, next_loc)
        self.location.pop()

    def render(self, screen):
        for x, y in self.location:
            pygame.draw.rect(screen, (0, 0, 200), (x, y, self.size, self.size))
