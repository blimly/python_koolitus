import pygame


class Snake:
    def __init__(self, start_x, start_y, game):
        self.window_size = game.window_size
        self.size = 20
        self.game = game
        self.location = [(start_x - self.size * i, start_y) for i in range(5)]
        self.dir = (1, 0)
        self.apple = None

    def update(self):
        next_loc = (self.location[0][0] + self.dir[0] * self.size, self.location[0][1] + self.dir[1] * self.size)
        self.location.insert(0, next_loc)
        last = self.location.pop()
        self.check_collision()
        if self.apple.x == next_loc[0] and self.apple.y == next_loc[1]:
            self.apple.eat()
            self.location.append(last)
            self.game.grow_apple()

    def render(self, screen):
        for x, y in self.location:
            pygame.draw.rect(screen, (0, 0, 200), (x, y, self.size, self.size))

    def check_collision(self):
        self.check_walls()
        self.check_body()

    def check_walls(self):
        head = self.location[0]
        if head[0] < 0 or head[1] < 0 or head[0] >= self.window_size[0] or head[1] >= self.window_size[1]:
            self.game.enter_state("end")

    def check_body(self):
        if len(self.location) != len(set(self.location)):
            self.game.enter_state("end")
