# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

# Системные переменные:
import time

__name__ = 'parser'
__author__ = 'Mine_Bit'
__file__ = 'gluinger.py'
__package__ = 'plugins'

# Функция склейки файлов:
def gluing(files_counter, array_file_names, output_file_name):
    global f_list
    i = 0
    full_line_counter = 0
    while i < files_counter:
        try:
            f = open(array_file_names[i])
            f_list = f.readlines()
            len_of_f_list = len(f_list)
            print('1')
        except IOError:
            print("Файл не найден!")
        if len_of_f_list == 0:
            print('Файл для чтения пуст!')
        else:
            counter_lines = 0
            while counter_lines < len_of_f_list:
                append_out_file = open(output_file_name, 'a')
                append_out_file.write(f_list[counter_lines])
                append_out_file.close()
                full_line_counter += 1
                counter_lines += 1
        i += 1


# Функция для старта склейки:
def run_gluing():
    files_counter = 0
    array_file_names = []
    output_file_name = None
    print('Запушен модуль "Склейщик" | Версия модуля: 0.2')
    while True:
        print('Меню модуля "Склейщик":')
        print('[0] - Просмотреть значения')
        print('[1] - Настроить значения')
        print('[2] - Запустить выполнение модуля')
        print('[777] - Выйти из модуля')
        input_int = int(input('>>'))
        if input_int == 0:
            print('Значения:')
            print('[0] - Файлы для склейки:')
            print(array_file_names)
            print('[1] - Имя файла результата: ', output_file_name)
        elif input_int == 1:
            while True:
                print('Настройка значений:')
                print('[0] - Файлы для склейки | Текущее количество: ', files_counter)
                print('[1] - Имя файла результата | Текущее значение: ', output_file_name)
                print('[777] - Выход из настроек')
                del input_int
                input_int = int(input('>>'))
                if input_int == 0:
                    while True:
                        print('Введите количество файлов для склейки:')
                        files_counter = int(input('>> '))
                        if files_counter <= 1:
                            print('Введенно неверное значение!')
                        else:
                            break
                    print('Вводите имена файлов построчно:')
                    i = 0
                    while i < files_counter:
                        while True:
                            input_file_name = str(input('>> '))
                            if len(input_file_name) != 0:
                                array_file_names.append(input_file_name)
                                break
                            else:
                                print('Ошибка ввода! Повторите операцию!')
                        i += 1
                    del i
                    print('Значения успешно присвоенны!')
                elif input_int == 1:
                    while True:
                        print('Введите имя выходного файла:')
                        output_file_name = str(input('>> '))
                        if len(output_file_name) != 0:
                            break
                        else:
                            print('Ошибка ввода! Повторите операцию!')
                    output_file = open(output_file_name, 'w')
                    output_file.write('Склеено с помощью BrainBruteKit 0.1 by brainhands.ru \n')
                    output_file.close()
                    print('Значения успешно присвоенны!')
                elif input_int == 777:
                    break
                else:
                    print('Ошибка ввода!')
        elif input_int == 2:
            print('Начинаем склейку...')
            start_time = time.time()
            gluing(files_counter, array_file_names, output_file_name)
            finish_time = time.time()
            print('Работа модуля "Склейка" завершен!')
            print('Время выполнения: ', str(finish_time - start_time), ' сек')
        elif input_int == 777:
            print('Выход из модуля "Склейка"...')
            break
