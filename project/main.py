import pygame

from interface import Interface
from shop import Shop
from Boss import Boss


class Main():
    def __init__(self):
        pygame.init()
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.interface = Interface()
        self.shop = Shop(self.screen, 0)
        self.boss = Boss(1)
        self.player_damage = 5
        self.damage_per_second = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.interface.draw(self.screen)
        self.boss.draw(self.screen)
        self.draw_hp_bar()

    def start(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                self.shop.start(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.try_to_click(event.pos)
        self.draw
        pygame.display.update()

    def try_to_click(self, pos):
        if 100 < pos[0] < 700 and 200 < pos[1] < 600:
            self.interface.seed.count += self.boss.bite(self.player_damage)

        def draw_hp_bar(self):
            k = self.Boss.hp / (50 * self.Boss.level)
            w = 400 * k
            pygame.draw.rect(self.screen, (0, 250, 0), (200, 100, int(w), 50), 0)


main = Main()
main.start()
