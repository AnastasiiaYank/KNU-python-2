# 10.4.Описати модуль та скласти програму для реалізації гри у “хрестики-нолики” на полі розміром 3x3. У модулі реалізувати дії:1) зробити хід гравця;2) зробити хід комп’ютера;3) показати ігрове поле.4) перевірити, чи закінчена гра, та повернути переможця, якщо є.

import random
field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = 'X'


def player_move():
    global current_player
    while True:
        x, y = input('Введіть координати: ')
        if not x in '123' or not y in 'abc':
            x, y = y, x
            if not x in '123' or not y in 'abc':
                print('Неправильні координати!')
                continue
        x = int(x)-1
        y = ord(y)-ord('a')
        if field[x][y] == ' ':
            field[x][y] = current_player
            current_player = 'O' if current_player == 'X' else 'X'
            break
        else:
            print('Це поле вже зайняте!')


def computer_move():
    global current_player
    moves = []
    for i in range(3):
        for j in range(3):
            if field[i][j] == ' ':
                moves.append((i, j))
    x, y = random.choice(moves)
    field[x][y] = current_player
    current_player = 'O' if current_player == 'X' else 'X'


def show_field():
    print('  | a | b | c |')
    for i in range(3):
        print(i+1, end=' |')
        for j in range(3):
            print(f' {field[i][j]} ', end='|')
        print()


def has_winner():
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != ' ':
            return field[i][0]
        if field[0][i] == field[1][i] == field[2][i] != ' ':
            return field[0][i]
    if field[0][0] == field[1][1] == field[2][2] != ' ':
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0] != ' ':
        return field[0][2]
    return None


def game_loop():
    winner = None
    while not winner:
        show_field()
        player_move()
        winner = has_winner()
        if winner:
            break
        computer_move()
        winner = has_winner()
    show_field()
    print(f'Переміг {winner}!')


game_loop()
