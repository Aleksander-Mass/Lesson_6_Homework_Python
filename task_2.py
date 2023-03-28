'''
Погружение в Python (семинары)
Урок 6. Модули

Задача 2.
=== Создайте модуль и напишите в нём функцию шахматный 
модуль. Внутри него напишите код, решающий 
задачу о 8 ферзях. Известно, что на доске 8×8 можно 
расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, 
есть ли среди них пара бьющих друг друга. 

===  Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
'''

__all__ = ['check_queens']


def check_queens(coordinates: list[tuple[int, int]]) -> bool:
    board = [[0 for _ in range(8)] for _ in range(8)]
    for row, col in coordinates:
        if board[row - 1][col - 1] != 0:
            return False
        for i in range(8):
            board[row - 1][i] = -1
            board[i][col - 1] = -1
            x = col - row + i
            if 0 <= x < 8:
                board[i][x] = -1
            x = col + row - 2 - i
            if 0 <= x < 8:
                board[i][x] = -1
        board[row - 1][col - 1] = 1
    return True


# run module
if __name__ == '__main__':
    # test = [(4, 1), (8, 2), (1, 3), (3, 4), (6, 5), (2, 6), (7, 7), (5, 8)]
    coordinates = []
    print('Введите координаты ферзей (ввод каждой пары через запятую)')
    for i in range(8):
        coord = tuple(map(int, input(f'{i + 1} пара: ').split(',')))
        coordinates.append(coord)

    # получаем ответ
    print(check_queens(coordinates))
