import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''Класс управления выстрелами из корабельной пушки'''

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.collor = self.settings.bullet_color

        # Создать rect выстрела в (0, 0) и задать правильную позицию
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Сохранять позицию выстрела как десятичное значение
        self.y = float(self.rect.y)

    def update(self):
        '''Продвигать выстрел вверх по экрану'''
        # Обновить десятичную позицию пули
        self.y -= self.settings.bullet_speed
        # Обновить позицию rect
        self.rect.y = self.y

    def draw_bullet(self):
        '''Отрисовать выстрел на экране'''
        pygame.draw.rect(self.screen, self.collor, self.rect)