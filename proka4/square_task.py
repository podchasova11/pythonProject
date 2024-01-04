# Написать функцию, которая принимает список,
# и возвращает этот же список, где все числа возведены в квадрат

def square(numbers):
    for number in range(len(numbers)):
        numbers[number] **= 2
    print(numbers)


numbers_list = [1, 2, 3, 4, 5]
square(numbers_list)
print(numbers_list)