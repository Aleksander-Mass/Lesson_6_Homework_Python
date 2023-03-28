'''
Погружение в Python (семинары)
Урок 6. Модули

Задача 3.
===   Напишите функцию в шахматный модуль. Используйте генератор 
случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''
import random

__all__ = ['get_random_queens', 'check_queens']

def get_random_queens() -> list[tuple[int, int]]:
    rows = random.sample(list(range(1, 9)), 8)
    columns = random.sample(list(range(1, 9)), 8)
    return list(zip(rows, columns))


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
    count = 0
    while count < 4:
        coordinates = get_random_queens()
        if check_queens(coordinates):
            print(f'{count + 1} правильная расстановка', coordinates)
            count += 1


