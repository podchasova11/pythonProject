# Домашнее задание  7
# Домашнее задание на тему "Циклы"
n = 0
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# Create a sample collection
users = {'Hans': 'active',
         'Éléonore': 'inactive',
         '景太郎': 'active'
         }

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(user)
        print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print(active_users)

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

fruits = ["apple", "banana", "pich"]
for fruit in fruits:
    print(fruit)
# Задание 1:
# Создайте пустой список и с помощью цикла 'for'
# заполните его числами от 0 до 100 (range в помощь).
# range(start, stop, step)
lists = []
for lists in range(0, 101, 20):
    print(lists)

message = "Hey, Im gonna go to work tommorow"
for letter in message:
    print(letter.upper())
    if letter == "g":
        print("KKKKKKKKKKKKKKKK")


person = {
    "name" : "Alexey",
     "age" : 25
}
print(person.items())
for k, v in person.items():
    print(k, v)

# for element in range(0, 101, 2):
#
#     lists.append(element)
#     print(f"Print {lists}")
# for element in lists:
#     print(f"Print {element}")



# Задание 2:
# С помощью цикла `while` необходимо удалять все элементы с
# конца списка сформированного в первом задании, до тех пор,
# пока общее количество элементов не станет 51.
counter = 0
for i in lists:
    if i < 52:
      lists.remove(i)
    counter += 1
    if counter == 52:
        break



# while counter <= 51:


# Результат должен получиться следующий [0, 1, 2, ...., 48, 49, 50].
# Задание 3:
# Используйте цикл `while` и инструкцию `break` для поиска первого числа,
# которое делится на 7, в диапазоне от 1 до 100.

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
