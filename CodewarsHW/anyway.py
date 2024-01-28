import datetime
print("Hi!")
print('It\'s so funny')
print(100)
print(100-300+25)
print("I am 20 years old.", "I am a student")
print("a,\nb,\nc")
print('*****')
print('*   *')
print('*   *')
print('*   *')
print('*****')

arr = [1, 2, 3, 4, 5, 6]
# print(mean(arr))
print((sum(arr) / len(arr)))

sec = int(input("введи время: "))
hour = sec // 3600 % 24
min_1 = sec // 60 % 60
num = min_1 // 10
num_2 = min_1 % 10
sec_1 = sec % 60
print(f'текущее время: {hour:0>2}:{num}{num_2}:{sec_1:0>2}')

print(100 / 2 ** 2)


# Write a function that takes an array of words and smashes them together
# into a sentence and returns the sentence.

def smash(words):
    string = ""
    for element in words:
        string += element
    return string
words = ["hello", "world"]
print(smash)

input_number = input("введи число: ")
pos_number = int(input_number) * -1
reverse_number = str(pos_number)[:: -1]
# final_number = int(input_number[0] + reverse_number)
print(int(input_number[0] + reverse_number))

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

print(greet('Johnny'))

def stringy(size):
    str = ''
    for i in range(size):
        if i % 2 == 0:
            str += '1'
        else: str += '0'
    return str
print(stringy(10))

def pipe_fix(nums):
    fix = []
    for i in range(len(nums)-1):
        if nums[i+1] != nums[1] + 1:
            fix.append(nums[i]+1)
        else:
            fix.append(nums[i])
    fix.append(nums[-1])
    return fix
result = pipe_fix([1, 2, 3, 5, 6, 8, 9])
print(result)

def split_and_merge(string_, separator):
    sp = list(string_)
    return str(sp)
print(split_and_merge("My name is John"," "))

a, b, c = map(str, input().split())
print(f'Simvol code {a} is {ord(a)}\nSimvol code {b} is {ord(b)}\nSimvol code {c} is {ord(c)}')

word = input().lower()
for el in word:
    if el in 'aoyuie':
        word = word.replace(el, '')
    else:
        word = word.replace(el, '.' + el)
print(word)

text = input()
result = ''
for el in text:
    if el.lower() in 'aeioyu':
        result += ''
    else:
        result += ('.' + el.lower())
print(result)

s = input().lower().replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '').replace('', '.')
print(s)
text = input()
print(f"|{text:&^20}|")
print(f"|{text:&<20}|")
print(f"|{text:&>20}|")

def split_and_merge(string_, separator):
    sp = list(string_)
    return (separator. join(sp)) # separator join()
print(split_and_merge("My name is John","-"))

def split_and_merge(string_, separator):
    sp = (string_.split())
    for i in range(len(sp)):
        sp[i] = separator. join(list(sp[i]))
    return ' '.join(sp)
print(split_and_merge("My name is John","-"))

def fake_bin(x):
    # a = ''
    for i in x:
        if int(i) <= 5:
            x = x.replace(i, "0") # i = '0'
        if int(i) > 5:
            x = x.replace(i, "1") # i = '1'
    return x
print(fake_bin("45385593107843568"))

class Person:
    def __init__(self, my_name):
        self.my_name = my_name

    def get_my_name(self):
        return self.my_name

    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.get_my_name()}'

def am_I_afraid(day,num):
    if day == 'Monday' and num == 12 or day == 'Tuesday' and num > 95 or day == 'Wednesday' and num == 34 or day == 'Thursday' and num == 0 or day == 'Friday' and num % 2 == 0 or day == 'Saturday' and abs(num) == 666:
        return True
    else:
        return False
print(am_I_afraid('Saturday',-666))

def to_jaden_case(string):
    string2 = " ".join(string.split())
    return string2.title().replace("'T", "'t")
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

def to_jaden_case(string):
    # string2 = string.replace("'", "-")
    return string.replace("'", "^").title().replace("^", "'")
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

def to_jaden_case(input_string):
    words = input_string.split()
    jaden_case_words = [word.capitalize() for word in words]
    return ' '.join(jaden_case_words)

def get_mean(arr,x,y):
    if x >= len(arr) or y >= len(arr):
        return -1
    else:
        sum1 = sum(arr[:x:])
        sum2 = sum(arr[-1:-y-1:-1])
        # return sum1, sum2
        return (sum1 / x) / 2 + (sum2 / y) / 2
        # print(sum1, sum2)
print(get_mean([1,3,2],2,2))

def remove_vowels(strng):
    for i in range(len(strng)):
        if strng[i] in 'aouie':
            strng = strng.replace(strng[i], '')
            return strng
print(remove_vowels('awquie'))

def remove_vowels(strng):
    res_str = ''.join(i for i in strng if i not in 'aeuio')
    return res_str
print(remove_vowels('awquie'))

def my_add(a, b):
    try:
        print(a + b)
    except:
        print("None")
my_add(1, "3.414")

def greet_jedi(first, last):
    return f'Greeetings, master {last[:3:].capitalize()}{first[:2:].capitalize()}'
print(greet_jedi('Beyonce', 'Knowles'))
def tidyNumber(n):
    if n % 10 > (n // 10) % 10:
        return True
    else:
        return False
print(tidyNumber(2789))

def tidyNumber(n):
    a = str(n)
    for i in range(1, len(a)):
        if a[i] < a[i+1]:
            return True
        else:
            return False
    return True
print(tidyNumber(9672))
# лучше решение +++++ >>
def tidyNumber(n):
    s = list(str(n))
    return s == sorted(s)

# preloaded variable: "dictionary"
dictionary = {
    'd': 'do',
    'f': 'foo',
    'h': 'hi'
}
def make_backronym(acronym):
    a = []
    for i in acronym:
        a.append(dictionary[i])
    return ' '.join(a)
print(make_backronym('dfh'))

def replace_nth(text, n, old_value, new_value):
    new_str = ''
    count = 0
    for i in text:
        if i == old_value:
            count += 1
            if n <= 0:
                new_str += i
            elif count % n == 0:
                new_str += new_value
            else:
                new_str += old_value
        else:
            new_str += i
    return new_str
print(replace_nth("Vader said: No, I am your cat!", 2, 'a', 'o'))