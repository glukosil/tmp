#!/usr/bin/python3

board = [' '] * 9 # игровая доска
player = 'X' # Ход игрока
winList = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] # Выигрышные комбинации

# Вывод игрового поля
def Doska():
    print('\033[H\033[2JКонсольная игра \"Крестики-Нолики\"!\n\n    ПОЛЕ   \t\t НУМЕРАЦИЯ')
    for _ in range(3): print(f'{"-" * 11}\t\t{"-" * 11}\n {board[_*3]} | {board[_*3+1]} | {board[_*3+2]}\t\t {_*3+1} | {_*3+2} | {_*3+3}')
    print(f'{"-" * 11}\t\t{"-" * 11}\n\nХОД ИГРОКА: {player}')

# Функция ввода числа с проверкой
def Num(txt):
    _ = input(f'{txt}: ')
    if _.isnumeric() and 0 < int(_) < 10 and board[int(_) - 1] == ' ': return int(_)
    else: print(f'Ошибка ввода! Нужно ввести незанятую позицию от 1 до 9!\n'); return Num(txt)

# Игровой процесс
while True:
    Doska()
    board[Num('Выберите позицию для хода') - 1] = player
    for _ in winList:
        if board[_[0]] == board[_[1]] == board[_[2]] != ' ': Doska(); print(f'\n\nИГРА ОКОНЧЕНА!\nПобедил игрок: {player}'); exit()
    if ' ' not in board: Doska(); print('\n\nИГРА ОКОНЧЕНА!\nУ вас ничья!'); break
    if player == 'X': player = '0'
    else: player = 'X'
