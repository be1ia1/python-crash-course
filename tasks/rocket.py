import pygame
import sys

class Rocket:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rocket Game")

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == '__main__':
    rk = Rocket()
    rk.run_game()

