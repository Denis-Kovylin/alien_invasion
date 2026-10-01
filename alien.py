import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Класс представляющий одного пришелца из инопланетного флота'''
    def __init__(self, ai_game):
        '''Инициализировать пришельца и задать его текущее разположение'''
        super().__init__()
        self.screen = ai_game.screen

        # Загрузить изображение пришельца и задать его rect атрибут
        self.image = pygame.image.load('images/alien_yellow.png')
        self.rect = self.image.get_rect()

        # Создавать каждого пришелца в левой верхней части экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Размещать пришельцев по горизонтали
        self.x = float(self.rect.x)