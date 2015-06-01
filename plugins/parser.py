# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

# Системные переменные:
__name__ = 'parser'
__author__ = 'Mine_Bit'
__file__ = 'parser.py'
__package__ = 'plugins'

# Импорты пакетов и библиотек:
import os
import time

# Функция выполнения парсинга. Пришлось вывести в функцию, чтобы измерить время выполнения парсинга.
def parse(out_file, len_of_f_list, f_list) -> object:
    out_file_names = (out_file + '_gmail.txt', out_file + '_yandex.txt', out_file + '_ya.txt', out_file + '_mail.txt',
                      out_file + '_inbox.txt', out_file + '_list.txt', out_file + '_bk.txt', out_file + '_lenta.txt',
                      out_file + '_rambler.txt', out_file + '_autorambler.txt', out_file + '_myrambler.txt',
                      out_file + '_ro.txt', out_file + '_r0.txt', out_file + '_yahoo.txt', out_file + '_outlook.txt',
                      out_file + '_hotmail.txt', out_file + '_else.txt')
    i = 0
    while i < len_of_f_list:
        for c in range(0, 16):
            if utill.domain_list[c] in f_list[i]:
                if not utill.files_created[c]:
                    gmail_out_flie = open(out_file_names[c], 'w')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
                    utill.files_created[c] = True
                else:
                    gmail_out_flie = open(out_file_names[c], 'a')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
            else:
                if not utill.files_created[16]:
                    gmail_out_flie = open(out_file_names[16], 'w')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
                    utill.files_created[16] = True
                else:
                    gmail_out_flie = open(out_file_names[16], 'a')
                    gmail_out_flie.write(f_list[i])
                    gmail_out_flie.close()
        i += 1
        print('Работа завршена!')


# Функция для старта парсинга:
def run_parse():
    f_list = None
    out_file = None
    file_to_parse = None
    print('|' + '=' * 33 + '|')
    print('| Плагин "Парсер"                 |')
    while True:
        print('|' + '=' * 33 + '|')
        print('| Меню плагина "Парсер":          |')
        print('| [0] - Просмотреть значения      |')
        print('| [1] - Настроить значения        |')
        print('| [2] - Запуск                    |')
        print('| [777] - Выйти из плагина        |')
        print('|' + '=' * 33 + '|')
        input_n = input('>>')
        if input_n == '0':
            print('Значения:')
            print('[0] - Файл для парсинга: ', file_to_parse)
            print('[1] - Основа имени файла для результата: ', out_file)
        elif input_n == '1':
            while True:
                print('Настройки значений:')
                print('[0] - Файл для парсинга | Текущее значение: ', file_to_parse)
                print('[1] - Основа имени файла для результата | Текущее значение: ', out_file)
                print('[777] - Выход из настроек')
                del input_n
                input_n = input('>>')
                if input_n == '0':
                    print('Введите новое имя файла для парсинга:')
                    file_to_parse = str(input('>>'))
                    print('Новое значение присвоено!')
                elif input_n == '1':
                    print('Введите основу имени файла для результата:')
                    print('!ВНИМАНИЕ! Данное значение не должно содержать расширение файла!')
                    out_file = input('>> ')
                    print('Новое значение присвоено!')
                elif input_n == '777':
                    break
                else:
                    print('Ошибка ввода!')
        elif input_n == '2':
            print('Проверяем значения:')
            try:
                f = open(file_to_parse)
                f_list = f.readlines()
                len_of_f_list = len(f_list)
            except IOError:
                print("Файл не найден!")
            if len_of_f_list == 0:
                print('Файл для чтения пуст!')
            else:
                file_size = os.path.getsize(file_to_parse)
                print('Информация о входном файле:')
                print('Имя файла: ', file_to_parse)
                print('Количество аккаунтов: ', str(len_of_f_list))
                print('Обьем файла: ' + str(file_size) + ' байт')
                print('Информация о выходном файле:')
                print('Имя файла: ', out_file)
                print('Все значения проверены. Парсинг запущен!')
                start_time = time.time()
                parse(out_file, len_of_f_list, f_list)
                finish_time = time.time()
                print('Парсинг завершен!')
                print('Время выполнения: ', str(finish_time - start_time), ' сек')
        elif input_n == '777':
            print('Выход из модуля "Парсинг"...')
            break
        else:
            print('Ошибка ввода!')
