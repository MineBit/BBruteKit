# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

# Системные переменные:
__name__ = '__main__'
__author__ = 'Mine_Bit'
__version__ = '0.2'
__file__ = 'bbrutekit.py'

# Импорты пакетов и билиотек:
import sys

from plugins import parser
from plugins import gluinger
from plugins import generator

# Метод для показа главного меню. Возвращает char значение выбранного пользователем элемента:
def show_menu():
    print('|=================================|')
    print('| МЕНЮ                            |')
    print('|=================================|')
    print('| Выберите опцию:                 |')
    print('| [1] Парсер баз аккаунтов        |')
    print('| [2] Склейщик баз паролей        |')
    print('| [3] Генератор словарей          |')
    print('| [4] Брутфорс                    |')
    print('| [h] Помощь                      |')
    print('| [i] Информация                  |')
    print('| [x] Выход                       |')
    print('|=================================|')
    return input('>> ')


# Основная функция программы:
def main():
    print('|' + '=' * 33 + '|')
    print('|  BBruteKit |', __version__, '| by', __author__, ' |')
    print('|   утилита для bruteforse атак   |')
    print('| Официальный сайт: brainhands.ru |')
    print('|' + '=' * 33 + '|')
    print('''
|=================================|
|                                 |
|  |=========|      |=========|   |
|  |          |     |          |  |
|  |          |     |          |  |
|  |         |      |         |   |
|  |========|       |========|    |
|  |         |      |         |   |
|  |          |     |          |  |
|  |          |     |          |  |
|  |=========|      |=========|   |
|                                 |
|=================================|
    ''')
    print()

# Запуск программы:
if __name__ == '__main__':
    main()
    while True:
        menu_item = show_menu()
        if menu_item == '1':
            parser.run_parse()
        elif menu_item == '2':
            gluinger.run_gluing()
        elif menu_item == '3':
            generator.run_generate()
        elif menu_item == '4':
            pass
        elif menu_item == 'h':
            pass
        elif menu_item == 'i':
            pass
        elif menu_item == 'x':
            print('Спасибо за использование программы!')
            print('По всем вопросам пишите сюда: mine_bit@brainhands.ru')
            sys.exit(1)
