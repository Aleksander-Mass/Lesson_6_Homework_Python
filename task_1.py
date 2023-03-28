'''
Погружение в Python (семинары)
Урок 6. Модули

Задача 1.
=== Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY

=== Функция возвращает истину, если дата может 
существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть 
в диапазоне [1, 9999].

=== Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.   (Наш календарь, сейчас 26 марта 2023 года, 365 дней в году, примерно раз в 4 года год високосный 366 дней в году, за исключением когда дата кратна 100, но не кратно 400)


=== Проверку года на високосность вынести в отдельную
защищённую функцию. (високосным годом будет считаться 
год кратный 4 и 400. Год кратный 100 не считается високосным).

===   В модуль с проверкой даты добавьте возможность 
запуска в терминале с передачей даты на проверку.
'''



from sys import argv

__all__ = ['is_exist']


def is_exist(input_date: str) -> bool:
    day, month, year = list(map(int, input_date.split('.')))

    if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
        match month:
            case 4 | 6 | 9 | 11:
                if day == 31:
                    return False
            case 2:
                if day == 29 and not _is_leap_year(year) or day > 29:
                    return False
                return True
            case _:
                return True
    return False


# проверка года на високосность
def _is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


# run module
if __name__ == '__main__':
    if len(argv) == 2:
        print(is_exist(argv[1]))
    else:
        input_date = input('Введите дату в формате DD.MM.YYYY ')
        print(is_exist(input_date))