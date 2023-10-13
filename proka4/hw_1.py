# Форматированные строковые литералы

#В следующем примере число Пи округляется до трех знаков после запятой:

import math
print(f'The value of pi is approximately {math.pi:.3f}.')

# Передача целого числа после ':'приведет к тому, что это поле будет иметь
# минимальное количество символов. Это полезно для выравнивания столбцов.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

# Спецификатор =можно использовать для расширения выражения до текста выражения, знака равенства, а затем представления вычисленного выражения:


bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')

#  Метод String format()

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

