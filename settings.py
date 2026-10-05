
class Settings:
    '''Класс для сохранения всех настроек игры'''

    def __init__(self):
        '''Инициализировать настройки игры'''
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (15, 15, 35)

        # Настройки выстрелов
        self.bullet_speed = 12
        self.bullet_width = 6
        self.bullet_height = 35
        self.bullet_color = (252, 82, 3)
        self.bullet_allowed = 3

        # Настройки корабля
        self.ship_speed = 8

        # Настройки пришелца
        self.alien_speed = 3.0
        self.fleet_drop_speed = 40
        # '1' - move_left; '-1' - move_right;
        self.fleet_direction = 1