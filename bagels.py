#!/usr/bin/python3

import random

const		= 4		# Разрядность строки
pitka		= 20		# Количество попыток
skaz		= ['НЕ УГАДАНО', 'УГАДАНО', 'РЯДОМ'] # Статусы угадывания букв
ugad		= [0] * const	# Массив со статусом каждой буквы секретного слова
sec = buk = old	= ''		# sec - загаданная последовательность, buk - использованные в игре буквы, old - предыдущий ввод
hide		= '#' * const	# подсказка с выводом угаданных в слове букв
while len(sec) < const: sec += chr(random.randint(65, 90)) # Придумываем секретную последовательность

# Функция ввода числа с проверкой
def Num(txt):
    _ = input(f'{txt}: ')
    if _ == '0': print('\nВы завершили игру. До встречи!'); exit()
    if _.isalpha() and len(_) == const: return _.upper()
    else: print(f'Ошибка ввода! Нужно ввести {const}-значную строку из букв A-Z!'); return Num(txt)

# Проверка хода
def Proverka(txt, ind):
    if txt == sec: print(f'\n\nВЫ ВЫИГРАЛИ!\nУгаданное слово: {sec}\nЧисло попыток: {ind}'); exit()
    global hide, buk, old
    for _ in range(const):
       if txt[_] == sec[_]: ugad[_] = 1; hide = hide[:_] + txt[_] + hide[_ + 1:]
       elif txt[_] in sec: ugad[_] = 2;
       else: ugad[_] = 0
       if txt[_] not in buk: buk += f' {txt[_]}'
    old = txt

# Игрооой процесс
def main():
    for x in range(pitka):
       print(f'\033[H\033[2JКонсольная игра "БЕЙЗЛ 2.0"!\n\nЗагаданная {const}-значная последовательность букв A-Z: {hide}\nПопыток: {pitka}\n\nПОДСКАЗКА:\nИспользованные буквы:{buk}\nПредыдущий ход: {old}\n\nРЕЗУЛЬТАТ ХОДА:\n|', end='')
       for _ in range(const): print(f'{skaz[ugad[_]].center(12)}|', end = '')
       Proverka(Num(f'\n\nПОПЫТКА {x + 1}:\nВведите предполагаемую {const}-значную последовательность (0 - для выхода)'), x)
    print('\n\nВЫ ПРОИГРАЛИ!\nЗакончились попытки!\nБыло загадано слово: {sec}')

if __name__ == '__main__':  main()
