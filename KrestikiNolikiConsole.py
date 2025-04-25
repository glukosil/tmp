#!/usr/bin/python3

import os

board = [' '] * 9 # игровая доска
player = 'X' # Ход игрока
winList = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] # Выигрышные комбинации

# Вывод игрового поля
def Doska():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Консольная игра \"Крестики-Нолики\"!')
    print('\n  ПОЛЕ   \t\t НУМЕРАЦИЯ')
    for _ in range(3):
       print('-' * 9, '\t\t', '-' * 9)
       print(f'{board[_*3]} | {board[_*3+1]} | {board[_*3+2]}\t\t {_*3+1} | {_*3+2} | {_*3+3}')
    print('-' * 9, '\t\t', '-' * 9, f'\n\nХОД ИГРОКА: {player}')

# Функция ввода числа с проверкой
def Num(txt):
    while True:
        _ = input(f'{txt}: ')
        if _.isnumeric():
           if 0 < int(_) < 10 and board[int(_) - 1] == ' ': return int(_)
           else: print(f'Ошибка: Введите незанятую позицию от 1 до 9!\n')
        else: print('Ошибка: Введенные данные не содержат чило!\n')

# Игровой процесс
while True:
    Doska()
    board[Num('Выберите позицию для хода') - 1] = player
    for _ in winList:
        if board[_[0]] == board[_[1]] == board[_[2]] != ' ': Doska(); print(f'\n\nИГРА ОКОНЧЕНА!\nПобедил игрок: {player}'); exit()
    if ' ' not in board: Doska(); print('\n\nИГРА ОКОНЧЕНА!\nУ вас ничья!'); exit()
    if player == 'X': player = '0'
    else: player = 'X'
