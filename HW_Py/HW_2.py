# Задание 2.1
# Напишите программу, которая проверяет
# здоровье персонажа в игре.
# Если оно равно или меньше нуля,
# выведите на экран False, в противном случае True.

hp = int(input('Пожалуйста введите ваши очки :'))
if hp > 0:
    print('True')
else:
    print('False')

# Задание 2.2
# Напишите программу, которая проверяет
# является ли введенное число четным.
# Если да, выведите на экран текст “Четное”,
# а иначе - “Нечетное”

num = int(input('Enter a number:'))
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
num = int(input('Enter a number:'))
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# Задание 2.3
# Напишите программу, которая проверяет
# является ли год високосным. Таковыми считаются года,
# которые делятся без остатка на 4 (2004, 2008) и не
# являются столетиями (500, 600). Однако, если год делится
# без остатка на 400, он также считается високосным (1200, 2000)

year = int(input('Введите год :'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Високосный год')
        else:
            print('Невисокосный год')
    else:
        print('Високосный год')
else:
    print('Невисокосный год')

year = int(input('Введите год :'))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('Високосный год')
else:
    print('Невисокосный год')

# Задание 2.4
# Напишите программу, которая печатает введенный
# текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью input()

text = input('Введите текст :')
num = int(input('Введите количество повторов :'))
i = 0
while i < num:
    print(text)
    i += 1

text = input('Введите текст :')
num = int(input('Введите количество повторов :'))
for i in range(num):
    print(text)


# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа
# и оператор (в формате str), производит заданное арифметическое
# действие и печатает результат в формате: {num1} {operator) {num2) = {result}

num1 = int(input('Введите число :'))
num2 = int(input('Введите число :'))
operator = input('Введите любой оператор : ( + - * ** / // % ) : ')
result = 0
if operator == '/':
    result = num1/num2
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '//':
    result = num1 // num2
elif operator == '%':
    result = num1 % num2
print(f'{num1} {operator} {num2} = {result}')


# health = int(input('Enter the level of health: '))
# if health <= 0:
#     print(False)
# else:
#     print(True)

''' 2 '''
# number = int(input('Enter the number: '))
# if number % 2 == 0:
#     print('Четное')
# if number % 2 != 0:
#     print('Нечетное')

''' 3 '''
# year = int(input('Enter the year: '))
# I Variant
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(True)
# else:
#     print(False)

# II Variant
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print(True)
# else:
#     print(False)

'''      4        '''
# text = input('Please enter your text: ')
# num = int(input('How many times should I print? '))
# for i in range(num):
#     print(text)
#
# '''   5   '''
#
# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# oper = input('Choose the operator: 1. Plus, 2. Minus, 3. Multi, 4. Divide: ')
# if oper == '1':
#     result = num1 + num2
#     print(f'{num1} + {num2} = {result}')
# elif oper == '2':
#     result = num1 - num2
#     print(f'{num1} - {num2} = {result}')
# elif oper == '3':
#     result = num1 * num2
#     print(f'{num1} * {num2} = {result}')
# elif oper == '4':
#     result = num1 / num2
#     print(f'{num1} / {num2} = {result}')
# else:
#     print('Something went wrong!!!')

