import pygame


class Snake:
    def __init__(self, start_x, start_y, game):
        self.window_size = game.window_size
        self.size = 20
        self.corner_size = 8
        self.game = game
        self.location = [(start_x - self.size * i, start_y) for i in range(5)]
        self.dir = (1, 0)
        self.apple = None
        self.body_colour = (0, 0, 200)
        self.corner_names = {  # First is for smooth, second is for rough
            "ul": [(self.corner_size, self.corner_size), (0, 0)],
            "ur": [(self.size - self.corner_size, self.corner_size), (self.size - self.corner_size, 0)],
            "dl": [(self.corner_size, self.size - self.corner_size), (0, self.size - self.corner_size)],
            "dr": [(self.size - self.corner_size, self.size - self.corner_size), (self.size - self.corner_size, self.size - self.corner_size)]
        }
        self.dir_corners = {
            (0, 1): ["dl", "dr"],
            (0, -1): ["ul", "ur"],
            (1, 0): ["ur", "dr"],
            (-1, 0): ["ul", "dl"]
        }
        self.turn_corners = {
            (0, 1): {
                (1, 0): "ul",
                (-1, 0): "ur"
            },
            (0, -1): {
                (1, 0): "dl",
                (-1, 0): "dr"
            },
            (1, 0): {
                (0, 1): "ul",
                (0, -1): "dl"
            },
            (-1, 0): {
                (0, 1): "ur",
                (0, -1): "dr"
            }
        }

    @staticmethod
    def dir_reverse(dir):
        return - dir[0], - dir[1]

    def update(self):
        next_loc = (self.location[0][0] + self.dir[0] * self.size, self.location[0][1] + self.dir[1] * self.size)
        self.location.insert(0, next_loc)
        last = self.location.pop()
        self.check_collision()
        if self.apple.x == next_loc[0] and self.apple.y == next_loc[1]:
            self.apple.eat()
            self.location.append(last)
            self.game.grow_apple()

    def render_tile(self, screen, x, y, smooth_corners):
        pygame.draw.rect(screen, self.body_colour, (x, y + self.corner_size, self.corner_size, self.size - 2 * self.corner_size))
        pygame.draw.rect(screen, self.body_colour, (x + self.corner_size, y, self.size - 2 * self.corner_size, self.size))
        pygame.draw.rect(screen, self.body_colour, (x + self.size - self.corner_size, y + self.corner_size, self.corner_size, self.size - 2 * self.corner_size))
        for corner, dists in self.corner_names.items():
            if corner in smooth_corners:
                self.draw_smooth(screen, x, y, dists[0][0], dists[0][1])
            else:
                self.draw_rough(screen, x, y, dists[1][0], dists[1][1])

    def draw_smooth(self, screen, x, y, dx, dy):
        pygame.draw.circle(screen, self.body_colour, (x + dx, y + dy), self.corner_size)

    def draw_rough(self, screen, x, y, dx, dy):
        pygame.draw.rect(screen, self.body_colour, (x + dx, y + dy, self.corner_size, self.corner_size))

    def draw_triangle(self, screen, x, y, dir):
        if dir == (0, 1):
            pygame.draw.polygon(screen, self.body_colour, ((x + self.size // 2, y), (x, y + self.size), (x + self.size, y + self.size)))
        elif dir == (0, -1):
            pygame.draw.polygon(screen, self.body_colour, ((x + self.size // 2, y + self.size), (x, y), (x + self.size, y)))
        elif dir == (1, 0):
            pygame.draw.polygon(screen, self.body_colour, ((x, y + self.size // 2), (x + self.size, y), (x + self.size, y + self.size)))
        elif dir == (-1, 0):
            pygame.draw.polygon(screen, self.body_colour, ((x + self.size, y + self.size // 2), (x, y), (x, y + self.size)))

    def render(self, screen):
        counter = 0
        for x, y in self.location:
            if counter == 0:
                self.render_tile(screen, x, y, self.dir_corners[self.dir])
            elif counter == len(self.location) - 1:
                prev_loc = self.location[counter - 1]
                dir = ((prev_loc[0] - x) // self.size, (prev_loc[1] - y) // self.size)
                self.draw_triangle(screen, x, y, dir)
            else:
                next_loc = self.location[counter + 1]
                prev_loc = self.location[counter - 1]
                d_next = ((next_loc[0] - x) // self.size, (next_loc[1] - y) // self.size)
                d_prev = ((prev_loc[0] - x) // self.size, (prev_loc[1] - y) // self.size)
                self.render_tile(screen, x, y, self.turn_corners[d_next][d_prev] if d_prev in self.turn_corners[d_next].keys() else [])
            counter += 1

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
