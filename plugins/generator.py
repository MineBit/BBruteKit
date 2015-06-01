# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

# Системные переменные:
import time

__name__ = 'generator'
__author__ = 'Mine_Bit'
__file__ = 'generator.py'
__package__ = 'plugins'

import string


def dic_generate(ids_in, min_symb, max_symb, f_name, pass_amount):
    abc = ''
    alphs = {'1': string.ascii_uppercase, '2': string.ascii_lowercase, '3': string.digits, '4': string.punctuation}
    # Создание алфавита;
    for n in ids_in:
        abc = abc + alphs[n]
    p_num = 0
    f_num = 0
    f = open((f_name + str(f_num) + '.txt'), 'w')
    for curlength in range(min_symb, max_symb + 1):  # Перебор длин паролей в заданном диапазоне;
        password = []  # Обнуление пароля;
        for i in range(curlength):
            password.append(0)
            if p_num == pass_amount:  # Запись в новый файл при необходимости.
                f.close()
                f_num += 1
                f = open((f_name + str(f_num) + '.txt'), 'w')
                p_num = 0
        cpass = ''
        for i in password:
            cpass += abc[i]
        f.write(cpass + '\n')
        p_num += 1
        contr = [len(abc) - 1 for x in password]  # Создание контольного значения;
        while password != contr:  # Пока не закончатся комбинации;
            password[len(password) - 1] += 1  # Прибавление единицы в конец списка;
            if len(abc) in password:  # Переход единицы на следующий уровень;
                j = len(password) - 1
                while len(abc) in password:
                    password[j] = 0
                    password[j - 1] += 1
                    j += -1
            if p_num == pass_amount:  # Запись в новый файл при необходимости.
                f.close()
                f_num += 1
                f = open((f_name + str(f_num) + '.txt'), 'w')
                p_num = 0
            cpass = ''
            for i in password:
                cpass += abc[i]
            f.write(cpass + '\n')
            p_num += 1
    f.close()
    print('Пароли сохранены в ' + f_name + '*_' + str(f_num) + '.txt')


def run_generate():
    IDs = '1'
    min_symb = 0
    max_symb = 0
    f_name = None
    pass_amount = 100000
    print('|' + '=' * 33 + '|')
    print('| Плагин "Генератор"              |')
    while True:
        print('|' + '=' * 33 + '|')
        print('| Меню плагина "Генератор":       |')
        print('| [0] - Просмотреть значения      |')
        print('| [1] - Настроить значения        |')
        print('| [2] - Запуск                    |')
        print('| [777] - Выйти из плагина        |')
        print('|' + '=' * 33 + '|')
        input_int = int(input('>> '))
        if input_int == 0:
            print('Значения:')
            print('[0] - Наборы символов: ', IDs)
            print('[1] - Минимальная длина пароля: ', min_symb)
            print('[2] - Максимальная длина пароля: ', max_symb)
            print('[3] - Название словаря: ', f_name)
            print('[4] - Количество паролей в каждой части словаря: ', pass_amount)
        elif input_int == 1:
            while True:
                print('Настроки значений:')
                print('[0] - Наборы символов | Текущее значение: ', IDs)
                print('[1] - Минимальная длина пароля | Текущее значение: ', min_symb)
                print('[2] - Максимальная длина пароля | Текущее значение: ', max_symb)
                print('[3] - Название словаря | Текущее значение: ', f_name)
                print('[4] - Количество паролей в каждой части словаря | Текущее значение: ', pass_amount)
                print('[777] - Выход из настроек')
                input_int = int(input('>> '))
                if input_int == 0:
                    print('Введите подряд номера наборов символов:')
                    print('[1] - EN (большие)')
                    print('[2] - en (маленькие)')
                    print('[3] - Цифры')
                    print('[4] - Пунктуационные знаки')
                    IDs = input('>> ')
                elif input_int == 1:
                    print('Задайте минимальное количество символов в паролях:')
                    min_symb = int(input('>> '))
                elif input_int == 2:
                    print('Задайте максимальное количество символов в паролях:')
                    max_symb = int(input('>> '))
                elif input_int == 3:
                    print('Назовите получаемый словарь:')
                    f_name = input('>> ')
                elif input_int == 4:
                    print('Введите количество паролей в каждой части словаря:')
                    pass_amount = int(input('>> '))
                elif input_int == 777:
                    break
                else:
                    print('Ошибка ввода!')
        elif input_int == 2:
            start_time = time.time()
            dic_generate(IDs, min_symb, max_symb, f_name, pass_amount)
            finish_time = time.time()
            print('Работа модуля "Генератор Словарей" завершена!')
            print('Время выполнения: ', str(finish_time - start_time), ' сек')
        elif input_int == 777:
            print('Выход из модуля "Генератор Словарей"...')
            break
        else:
            print('Ошибка ввода!')
