# -*- coding: utf-8 -*-
# Coded by Mine_Bit[BrainHands]
# brainhands.ru
# mine_bit@brainhands.ru


# Массив, который будет хранить инфромацию, созданы ли файлы:
files_created = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False, False, False]

# Кортеж, который содержит константы с доменами, для парсинга почт:
domain_list = (
    '@gmail.com', '@yandex.ru', '@ya.ru', '@mail.ru', '@inbox.ru', '@list.ru', '@bk.ru', '@lenta.ru', '@rambler.ru',
    '@autorambler.ru', '@myrambler.ru', '@ro.ru', '@r0.ru', '@yahoo.com', '@outlook.com', '@hotmail.com', None)

# Памятка  по значениям индексов кортежа:
# [0] - Gmail (@gmail.com)
# [1] - Yandex (@yandex.ru)
# [2] - Yandex (@ya.ru)
# [3] - Mail (@mail.ru)
# [4] - Mail (@inbox.ru)
# [5] - Mail (@list.ru)
# [6] - Mail (@bk.ru)
# [7] - Rambler (@lenta.ru)
# [8] - Rambler (@rambler.ru)
# [9] - Rambler (@autorambler.ru)
# [10] - Rambler (@myrambler.ru)
# [11] - Rambler (@ro.ru)
# [12] - Rambler (@r0.ru)
# [13] - Yahoo! (@yahoo.com)
# [14] - Microsoft (@outlook.com)
# [15] - Microsoft (@hotmail.com)
# [16] - Нераспознаное
