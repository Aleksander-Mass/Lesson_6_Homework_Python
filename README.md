# Погружение в Python (семинары)
## Урок 6. Модули

# Задача 1.
=== Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY

=== Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне
[1, 9999].

=== Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.   (Наш календарь, сейчас 26 марта 2023 года, 365 дней в году, примерно раз в 4 года год високосный 366 дней в году, за исключением когда дата кратна 100, но не кратно 400)


=== Проверку года на високосность вынести в отдельную
защищённую функцию. (високосным годом будет считаться год кратный 4 и 400. Год кратный 100 не считается високосным).

===   В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


### Задача 2.
=== Создайте модуль и напишите в нём функцию шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 

===  Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

### Задача 3.
===   Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

# Преподаватель ждет ваше задание до 31 марта, 20:00 +03:00 UTC