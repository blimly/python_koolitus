import pygame


class Menu:
    def __init__(self, parent, parent_size):
        self.parent = parent
        self.parent_size = parent_size
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.buttons = {
            "game": ["Start game", (self.parent_size[0] // 2 - 100, self.parent_size[1] // 2 - 25, 200, 50)]
        }

    def event(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                self.parent.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.parent.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for name, button in self.buttons.items():
                    loc = button[1]
                    if loc[0] < x < loc[0] + loc[2] and loc[1] < y < loc[1] + loc[3]:
                        self.parent.start(name)

    def update(self):
        pass

    def render(self, window):
        window.fill((51, 151, 51))
        for name, button in self.buttons.items():
            text = pygame.transform.scale(self.font.render(button[0], False, (0, 0, 0)), (button[1][2], button[1][3]))
            pygame.draw.rect(window, (50, 50, 200), button[1])
            window.blit(text, (button[1][0], button[1][1]))
        pygame.display.update()

    def get_tick_length(self):
        return 10
