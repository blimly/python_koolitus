import pygame
import random
import math

from snake import Snake
from tree import Tree


class Game:
    def __init__(self, parent, window_size, player_amount):
        self.parent = parent
        self.window_size = window_size

        self.game_over_music_file = "game_over.wav"
        self.background_music_file = "expanse_terminal.wav"

        self.state = "game"
        self.end_counter = 0

        self.end_surface = pygame.Surface(self.window_size)
        self.end_surface.fill((255, 0, 0))
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.background_music_file), loops=-1)

        snake_dir = [1, -1]
        snake_x = [120, 520]
        snake_colours = [(0, 0, 200), (0, 200, 0)]
        self.snake_commands = {
            "up": [pygame.K_w, pygame.K_UP],
            "down": [pygame.K_s, pygame.K_DOWN],
            "right": [pygame.K_d, pygame.K_RIGHT],
            "left": [pygame.K_a, pygame.K_LEFT]
        }

        self.snakes = [Snake(snake_x[i], 120, self, snake_dir[i], snake_colours[i]) for i in range(player_amount)]
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
        snake_commands = [None for _ in self.snakes]
        for event in event_list:
            if event.type == pygame.QUIT:
                self.parent.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.enter_state("end")
                for command, keys in self.snake_commands.items():
                    for i, key in enumerate(keys):
                        if event.key == key:
                            snake_commands[i % len(self.snakes)] = command
        for snake, command in zip(self.snakes, snake_commands):
            if command is not None:
                snake.try_turn(command)

    def update(self):
        [snake.update() for snake in self.snakes]
        if self.state == "end":
            self.end_counter += 10
            if self.end_counter >= 200:
                pygame.mixer.Channel(0).pause()
                self.parent.close("game")

    def render(self, window):
        window.fill((51, 51, 51))
        [snake.render(window) for snake in self.snakes]
        [tree.render(window) for tree in self.trees]

        if self.state == "end":
            self.end_surface.set_alpha(self.end_counter)
            window.blit(self.end_surface, (0, 0))

        pygame.display.update()

    def grow_apple(self):
        self.apple = random.choice(self.trees).grow()
        for snake in self.snakes:
            snake.apple = self.apple

    def get_tick_length(self):
        return max(10, 1.4 * math.sqrt(sum([len(snake.location) for snake in self.snakes]) / len(self.snakes))) / len(self.snakes)
