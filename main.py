import pygame
from snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.end_counter = 0
        self.window = pygame.display.set_mode((640, 480))
        self.end_surface = pygame.Surface((640, 480))
        self.end_surface.fill((255, 0, 0))
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake(120, 120)

    def event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.dir = (1, 0)
                elif event.key == pygame.K_LEFT:
                    self.snake.dir = (-1, 0)
                elif event.key == pygame.K_DOWN:
                    self.snake.dir = (0, 1)
                elif event.key == pygame.K_UP:
                    self.snake.dir = (0, -1)

    def update(self):
        self.snake.update()

    def render(self):
        self.window.fill((51, 51, 51))
        self.snake.render(self.window)

        pygame.display.update()

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(6)


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
