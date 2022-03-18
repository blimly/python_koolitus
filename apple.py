import pygame


class Apple:
    def __init__(self, location, tree):
        self.eat_sound_effect_file = "munch-sound-effect.wav"
        self.location = location
        self.x, self.y = location[0] // 20 * 20, location[1] // 20 * 20
        self.tree = tree

    def render(self, screen):
        pygame.draw.circle(screen, (200, 0, 0), self.location, 5)

    def eat(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.eat_sound_effect_file))
        self.tree.branch()
