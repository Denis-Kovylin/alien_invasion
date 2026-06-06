
class Settings:
    '''Класс для сохранения всех настроек игры'''

    def __init__(self):
        '''Инициализировать настройки игры'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (15, 15, 35)

        # Настройки корабля
        self.ship_speed = 1.5