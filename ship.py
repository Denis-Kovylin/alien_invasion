import pygame

class Ship:
    '''Класс для управления караблем'''

    def __init__(self,ai_game):
        '''Инициализировать каробль и задать его изначальную позицию'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузить изображения корабля и получить его rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Создать каждый новый корабль внизу экрана по центру
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранить десятичное значение для позиции корабля по горизонтали
        self.x = float(self.rect.x)

        # Индикатор движения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Обновить текущую позицию корабля на основе индикатора движения'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновить объект rect с self.x
        self.rect.x = self.x

    def blitme(self):
        '''Отрисовать корабль в его текущем местоположении'''
        self.screen.blit(self.image, self.rect)
