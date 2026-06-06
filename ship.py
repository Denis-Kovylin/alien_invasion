import pygame

class Ship:
    '''Класс для управления караблем'''

    def __init__(self,ai_game):
        '''Инициализировать каробль и задать его изначальную позицию'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузить изображения корабля и получить его rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Создать каждый новый корабль внизу экрана по центру
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Отрисовать корабль в его текущем местоположении'''
        self.screen.blit(self.image, self.rect)
