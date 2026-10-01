import sys
import pygame
from  settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''Общий класс управляющий управляющий ресурсами и поведегием игры'''

    def __init__(self):
        '''Инициализирования игры, создание игровых ресурсов'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        print(self.settings.screen_width, self.settings.screen_height)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        '''Начать главный цикл игры'''
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_event(self):
        # Следить за событиями мыши и клавиатуры ( Диспечер Событий )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''Реагировать на нажатие клавиши'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Реагировать на отпуск клавиши'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Создать новый выстрел и добавить его в группу выстрелов'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet(self):
        '''Создать флот пришельцев'''
        # Создать пришельцев и выяснить их количество в одном ряду
        # Растояние между пришельцами ровняеться ширине одного пришельца
        alien = Alien(self)
        alien_width, alien_heigh = alien.rect.size

        print(alien_width, alien_heigh)

        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Вияснить, какое количество рядов пришельцев помещаеться на экране
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 2 * alien_heigh - ship_height
        number_rows = available_space_y // (2 * alien_heigh)

        # Создать полноценный флот пришелцев
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''Создать пришельца и поставить его в ряд'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
        alien.rect.y = alien.y

    def _update_screen(self):
        # Обновить изображение и переключиться на следующий экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Создать экземпляр игры и запустить игру
    ai = AlienInvasion()
    ai.run_game()