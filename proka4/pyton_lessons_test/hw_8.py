def sq(numbs):
    for numb in range(len(numbs)):
        numbs[numb] **= 2
    print(numbs)


list_n = [2, 0, 2, 8]
sq(list_n)


def square(numbers):
    for number in range(len(numbers)):  # number - это номер из полученного списка , а не само число
        numbers[number] **= 2          # поэтому numbers[number] все равно что numbers[0] или другой любой порядковый номер
    print(numbers)


number_list = [1, 2, 3, 4]
square(number_list)


def sumer(number):
    for nmb in range(len(number)):
        number[nmb] **= 2
    print(number)


nim_list = [1, 8]
sumer(nim_list)
