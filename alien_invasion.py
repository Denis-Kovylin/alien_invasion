import sys
import pygame
from  settings import Settings
from ship import Ship

class AlienInvasion:
    '''Общий класс управляющий управляющий ресурсами и поведегием игры'''

    def __init__(self):
        '''Инициализирования игры, создание игровых ресурсов'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        '''Начать главный цикл игры'''
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        # Следить за событиями мыши и клавиатуры ( Диспечер Событий )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Обновить изображение и переключиться на следующий экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Создать экземпляр игры и запустить игру
    ai = AlienInvasion()
    ai.run_game()