# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# ### Sort a Word (alphabet increasing ) using loop.
alpf = ["a","d","h"]
for let in range(len(alpf)): # сколько элементов в списке столько раз выполнится цикл
    print(let)
for let in alpf:
    print(let)


def pattern(char1=2, char2=2):

    return (char1 + char2) * 2

print(pattern)
#

lists = []

# заполните его числами от 0 до 100 (range в помощь).
for element in range(0, 101, 20):

    lists.append(element)
    print(f"Print {lists}")
for element in lists:
    print(f"Print {element}")
    print(lists)



# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
#
person = {
    "name": "John",
    "last_name": "Smith",
    "age": 35,
    "position": "web developer"
}
print(person.items())
for key, value in person.items():
    print(f" {key} :  {value}")

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
import math as m
counter = 0
my_list = [20, -3, 15, 2, -1, -21]
new_arr = m.prod(my_list)
print(new_arr)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# ВСТРОЕННЫЕ ФУНКЦИИ (BUILT-IN FUNCTIONS)
min_arg = min(5, 6, 8, 10)
print(min_arg)

# FUNCTIONS


def persons(age, last_name='Smith', name='Anna'):
    return f"Hello, my name is {name} {last_name}. I am {age} years old."
print(persons(name='Alce', age=30))


def pattern(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1

print(pattern(char1='/', length=9))

#
# ПРОСТРАНСТВО ИМЕН
# (Globals)


def sum_it(x=5, y=7):
    return x + y
print(f'Locals: {sum_it(15, 78)}')

print(f'Inside the function: {sum_it(5, 8)}')
print(f'Outside the function: {sum_it(224, 8)}')
print(f'Globals: {globals()}')


#SCOPE
name = 'Alice'


def outer_function():
    name = 'Alex'
    def inner_function():
        name = 'Albert'
        return name

    return inner_function

closure = outer_function()
result = closure()
print(result)

# DECORATORS
# def decorator_function(func):
#     def wrapper(*arg):
#         print('Функция-обёртка!')
#         print(f'Оборачиваемая функция: {func.__name__}')
#         print('Выполняем обёрнутую функцию...')
#         print(func(*arg))
#         print('Выходим из обёртки')
#
#     return wrapper
#
#
# @decorator_function
# def hello(item):
#     return f'{item} is wrapped!'
#
#
# hello('Candy')



# ВСТРОЕННЫЕ МОДУЛИ (BUILT-IN MODULES)
from math import *

import math as m

arr = [1, 2, 3, 4, 5, 10, 25]
new_arr = m.prod(arr)
print(new_arr)

import datetime
birth_year = 1980
current_date = datetime.date.today()
current_age = current_date.year - birth_year
current_month = current_date.month
print(current_date)
print(current_age)
print(current_month)

# LAMBDA FUNCTION
mult = lambda x, y, z: x * y * z
print(mult(5, 8, 2))



# print('------Sum list_1 With function and for loop----------')
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# def filter_and_sum_nums(l):
#     new_l = []
#     for i in l:
#         if isinstance(i, int):
#             new_l.append(i)
#     return sum(new_l)

#
# print(filter_and_sum_nums(list_1))
#
# print('--------Sum list_1 with lambda and filter----------')
print(sum((filter(lambda x: isinstance(x, int), list_1))))


#
#
# print('------Filter odd_nums with custom function----------')
# def take_odd(num):
#     if isinstance(num, int) and num%2:
#         return True
#     return False
#
# print(list(filter(take_odd, list_1)))
#
# list_3 = [1, 2, 5, 8, 10, 105, 78]
# print(list(filter(take_odd, list_3)))
#
# print('-----Filer odd_nums with lambda----------')
# filtered = list(filter(lambda x: isinstance(x, int), list_1))
# print(list(filter(lambda x: x%2, filtered)))
#
# print(list(filter(lambda x: x%2, list_3)))
#
# print('-----Filer strings with "a" using custom function ----------')
# new_l = []
# for item in list_1:
#     if isinstance(item, str) and 'a' in item:
#         new_l.append(item)
# print(new_l)
# #
# print('-----Filer strings with "a" using lambda ----------')
# filtered = list(filter(lambda x: isinstance(x, str) and 'a' in x, list_1))
# print(filtered)

# MODULES
# import functools
# from functools import reduce
# res = reduce(lambda x, y: x*y, [1, 5, 8, 11, 13])
# print(res)
#
# from my_file import *
# res = sum_it(5, 8)
# print(res)
#
# res1 = prod(5, 8)
# print(res1)
#
# CUSTOM MODULES

#my_module.py

#def sum_it(x, y):
#    return x + y


# from my_module import *
# def tests():
#     assert sum_it(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
#     assert sum_it(10, 15) == 26, f'Wrong number, actual result is {sum_it(10, 15)}'
#
# tests()

# def sum_it(**kwargs):
#     print(type(kwargs))
#     return sum(kwargs.values())
#
# print(sum_it(num1=4, num2=5, num3=10))
#
# def sum_args(*args):
#     print(type(args))
#     return sum(args)
# print(sum_args(5, 6, 10))
#
