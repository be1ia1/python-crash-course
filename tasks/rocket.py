import pygame
import sys

class Rocket:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rocket Game")
        self.rocket = Ship(self)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.rocket.mov_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.mov_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket.mov_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.mov_right = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.mov_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.mov_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.mov_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.mov_right = False

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

class Ship:
    def __init__(self, rk_game):
        self.screen = rk_game.screen
        self.screen_rect = rk_game.screen.get_rect()
        self.image = pygame.image.load('Daco_5228169-1.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.mov_right = False
        self.mov_left = False
        self.mov_up = False
        self.mov_down = False

    def update(self):
        if self.mov_up and self.rect.top > self.screen_rect.top:
            self.y -= 0.3
        elif self.mov_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 0.3
        elif self.mov_right and self.rect.right < 800:
            self.x += 0.3
        elif self.mov_left and self.rect.left > 0:
            self.x -= 0.3
        self.rect.y = self.y
        self.rect.x = self.x
        # pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    rk = Rocket()
    rk.run_game()

