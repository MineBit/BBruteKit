# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

# Системные переменные:
__name__ = 'bruteforse'
__author__ = 'Mine_Bit'
__file__ = 'bruteforse.py'
__package__ = 'plugins'


def run_ftp_brute():
    while True:
        host = None
        username = None
        passwords_file = None
        print('|' + '=' * 33 + '|')
        print('| Плагин "FTP брутфорс"               |')
        print('|' + '=' * 33 + '|')
        print('| [0] - Просмотреть параметры         |')
        print('| [1] - Изменить параметры            |')
        print('| [2] - Запуск                        |')
        print('| [777] - Выйти из плагина            |')
        print('|' + '=' * 33 + '|')
        input_s = input('>> ')
        if input_s == '0':
            print('|' + '=' * 33 + '|')
            print('| Параметры:                         |')
            print('|' + '=' * 33 + '|')
            print('Хост:', host)
            print('Логин: ', username)
            print('Файл с паролями: ', passwords_file)
            print('|' + '=' * 33 + '|')
        elif input_s == '1':
            while True:
                print('|' + '=' * 33 + '|')
                print('| Выберите параметр для изменения:  |')
                print('|' + '=' * 33 + '|')
                print('| [0] - Хост                        |')
                print('| [1] - Логин                       |')
                print('| [2] - Файл с паролями             |')
                print('| [777] - Выход из настроек         |')
                print('|' + '=' * 33 + '|')
                del input_s
                input_s = input('>> ')
                if input_s is '0':
                    while True:
                        print('Введите новое значение "Хост":')
                        host = input('>> ')
                        if host is not None:
                            print('Новое значение "Хост": ', host)
                            break
                        elif host is None:
                            print('Введенное значение пустрое!')
                elif input_s is '1':
                    while True:
                        print('Введите новое значение "Логин":')
                        username = input('>> ')
                        if username is not None:
                            print('Новое значение "Логин": ', username)
                            break
                        elif username is None:
                            print('Введенное значение пустое!')
                elif input_s is '2':
                    while True:
                        print('Введите новое значение "Файл с паролями":')
                        passwords_file = input('>> ')
                        if passwords_file is not None:
                            print('Новое значение "Файл с паролями": ', passwords_file)
                            break
                        elif passwords_file is None:
                            print('Введенное значение пустое!')
                            # ftp_brute_plugin_2.ftp_brute()


def show_bruteforse_menu():
    print('|' + '=' * 33 + '|')
    print('| Плагин "Брутфорс"               |')
    while True:
        print('|' + '=' * 33 + '|')
        print('| Меню плагина "Брутфорс":       |')
        print('| [0] - FTP брутфорс             |')
        print('| [1] - HTTP брутфорс            |')
        print('| [777] - Выйти из плагина       |')
        print('|' + '=' * 33 + '|')
        input_int = int(input('>>'))
        if input_int == 0:
            pass
        elif input_int == 1:
            pass
        elif input_int == 777:
            print('Выход из плагина "Брутфорс"...')
            break
