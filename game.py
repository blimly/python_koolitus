import pygame
import random
import math

from snake import Snake
from tree import Tree


class Game:
    def __init__(self, parent, window_size):
        self.parent = parent
        self.window_size = window_size

        self.game_over_music_file = "game_over.wav"
        self.background_music_file = "expanse_terminal.wav"

        self.state = "game"
        self.end_counter = 0

        self.end_surface = pygame.Surface(self.window_size)
        self.end_surface.fill((255, 0, 0))
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.background_music_file), loops=-1)

        self.snake = Snake(120, 120, self)
        self.apple = None
        self.trees = [
            Tree((320, 480), (0, -1), 50),
            Tree((0, 240), (1, 0), 50),
            Tree((320, 0), (0, 1), 50),
            Tree((640, 240), (-1, 0), 50)
        ]
        self.grow_apple()

    def enter_state(self, state):
        if state == "end":
            if self.state != "end":
                pygame.mixer.Channel(2).play(pygame.mixer.Sound(self.game_over_music_file))
        self.state = state

    def event(self, event_list):
        prev_dir = self.snake.dir
        for event in event_list:
            if event.type == pygame.QUIT:
                self.parent.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.enter_state("end")
                elif event.key == pygame.K_RIGHT and prev_dir != (-1, 0):
                    self.snake.dir = (1, 0)
                elif event.key == pygame.K_LEFT and prev_dir != (1, 0):
                    self.snake.dir = (-1, 0)
                elif event.key == pygame.K_DOWN and prev_dir != (0, -1):
                    self.snake.dir = (0, 1)
                elif event.key == pygame.K_UP and prev_dir != (0, 1):
                    self.snake.dir = (0, -1)

    def update(self):
        self.snake.update()
        if self.state == "end":
            self.end_counter += 10
            if self.end_counter >= 200:
                pygame.mixer.Channel(0).pause()
                self.parent.close("game")

    def render(self, window):
        window.fill((51, 51, 51))
        self.snake.render(window)
        [tree.render(window) for tree in self.trees]

        if self.state == "end":
            self.end_surface.set_alpha(self.end_counter)
            window.blit(self.end_surface, (0, 0))

        pygame.display.update()

    def grow_apple(self):
        self.apple = random.choice(self.trees).grow()
        self.snake.apple = self.apple

    def get_tick_length(self):
        return max(10, 1.4 * math.sqrt(len(self.snake.location)))
