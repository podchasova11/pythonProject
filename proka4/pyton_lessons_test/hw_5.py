# Домашнее задание
# Домашнее задание на тему "Условные операторы и вложенные операторы":
#
# Задание 1:
# 1. Объявите переменную `num` и присвойте ей произвольное числовое значение.
num = 9
# 2. Используя условный оператор `if`, проверьте, является ли значение переменной `num` положительным.
# Если да, выведите сообщение "Число положительное".
if num >= 0:
    print("положительное число")

# 3. Добавьте блок `else` к условному оператору, чтобы вывести сообщение
# "Число отрицательное", если значение переменной `num` отрицательное.
else:
    print("отрицательное число")
# 4. Используйте вложенные условные операторы (`if`, `elif`, `else`) для определения диапазона числа `num`:
#   - Если `num` меньше 0, выведите сообщение "Число отрицательное".
#   - Если `num` равно 0, выведите сообщение "Число равно нулю".
#   - Если `num` больше 0 и меньше 10, выведите сообщение "Число от 1 до 9".
#   - Если `num` больше или равно 10, выведите сообщение "Число 10 и больше".
if num < 0:
    print("Число отрицательное")
elif num == 0:
    print("Число равно нулю")
elif num >= 10:
    print("Число 10 и больше")
else:
    if 0 < num < 10:
        print("Число от 1 до 9")


# Задание 2:
# 1. Объявите переменные `is_raining` и `is_sunny` и присвойте им логические значения `True` или `False`
# (в зависимости от погоды).
# 2. Используя логические операторы `and`, `or`, определите различные сценарии погоды:
#   - Если `is_raining` и `is_sunny` - выведите сообщение "Двойка вариантов, проверьте погоду!".
#   - Если `is_raining` или `is_sunny` - выведите сообщение "У нас хорошая погода!".
#   - Если `not is_raining` - выведите сообщение "У нас солнечная погода!".


is_raining = True
is_sunny = True
if is_raining is True and is_sunny is False:
    print("Whether is bad")
else:
    print("Whether is good")

if is_raining and is_sunny:
    print("Двойка вариантов, проверьте погоду!")
elif is_raining or is_sunny:
    print("У нас хорошая погода!")
elif not is_raining:
    print("У нас солнечная погода!")