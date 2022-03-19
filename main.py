import pygame
import math

from game import Game
from menu import Menu


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.window_size = (640, 480)
        self.window = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.running = True

        self.active_screen = "menu"
        self.screens = {
            "game": None,
            "menu": Menu(self, self.window_size)
        }

    def close(self, screen):
        if screen == "game":
            self.active_screen = "menu"

    def start(self, mode):
        if mode == "single player":
            self.screens["game"] = Game(self, self.window_size, 1)
        elif mode == "multiplayer":
            self.screens["game"] = Game(self, self.window_size, 2)
        self.active_screen = "game"

    def event(self):
        event_list = pygame.event.get()
        self.screens[self.active_screen].event(event_list)

    def update(self):
        self.screens[self.active_screen].update()

    def render(self):
        self.screens[self.active_screen].render(self.window)

    def run(self):
        while self.running:
            self.event()
            self.update()
            self.render()
            self.clock.tick(self.screens[self.active_screen].get_tick_length())


if __name__ == '__main__':
    main = Main()
    main.run()
    pygame.quit()
