# Импортируем модуль pygame для работы с графикой, импортируем модуль sys для доступа к системным функциям
import pygame, sys
# Импортируем тип Tuple из модуля typing для использования кортежей
from typing import Tuple

# Инициализация библиотеки pygame
pygame.init()

# Создание класса
class console:
    # Конструктор класса console
    def __init__(self, name: str, size: Tuple[int, int], bgcolor: Tuple[int, int, int], letter_color: Tuple[int, int, int]):
        # Установка названия окна
        pygame.display.set_caption(name)
        # Текст на экране
        self.screen_text = 'Input: '
        # Установка шрифта и размера
        self.font_style = pygame.font.SysFont('Consolas', 15)
        # Цвет фона
        self.bgcolor = bgcolor
        # Цвет букв
        self.letter_color = letter_color
        # Размер окна
        self.size = size
        # Создание окна
        self.dis = pygame.display.set_mode((size[0]*8, size[1]*15))

    # Метод для считывания ввода с клавиатуры
    def _get_input(self, hide_input: bool = False) -> str:
        out = ''
        while True:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Если нажата клавиша Enter
                    if event.key == pygame.K_RETURN:
                        self.screen_text += '\n'
                        return out
                    # Если нажата клавиша Backspace и текст на экране существует
                    elif event.key == pygame.K_BACKSPACE and self.screen_text:
                        out = out[:-1]
                        self.screen_text = self.screen_text[:-1]
                    # Вывод текста на экран консоли
                    elif event.unicode.isprintable():
                        out += '*' if hide_input else event.unicode
                        self.screen_text += event.unicode
                # Если окно закрыто
                elif event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit(0)
            # Заполнение экрана цветом
            self.dis.fill(self.bgcolor)
            # Вывод текста на экран
            for i, line in enumerate(self.screen_text.split('\n')[-self.size[1]:]):
                self.dis.blit(self.font_style.render(line, True, self.letter_color), (0, i*15))
            # Обновление экрана
            pygame.display.update()

    # Метод для отображения сканов (ввод не скрывается)
    def show_scans(self) -> str:
        return self._get_input(hide_input=False)

    # Метод для скрытого отображения сканов (ввод скрывается)
    def hidden_scans(self) -> str:
        return self._get_input(hide_input=True)

# Основной цикл программы
while True:
    print('User entered:', console('My console', (80, 25), (0, 0, 0), (255, 255, 255)).show_scans())
