import pygame
import sys


class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (166, 202, 240)
        self.character = Character(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            self.character.blitme()
            pygame.display.flip()

class Character:
    def __init__(self, bs_game):
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        self.image = pygame.image.load('panda-151605_640-1.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
