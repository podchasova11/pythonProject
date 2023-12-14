class Human:
    def __init__(self, gender, age, weight, height, eyes_color):
        self.gender = gender
        self.__age = age
        self.weight = weight
        self.height = height
        self.eyes_color = eyes_color

    def move(self):
        print('I can walk and run')

    def get_age(self):
        print(self.__age)

    def set_age(self, new_age):
        self.__age = new_age

    def super_mother(self):
        print('I can feed my family')

    def super_father(self):
        print('I can help my family')


person1 = Human('f', 36, 54, 154, 'brown')
person1.move()
print(person1.get_age())
print(person1.__dict__)
print(person1._Human__age)
person1.set_age(18)
print(person1.__dict__)
person1.weight = 45
person1._Human__age = 21
print(person1.__dict__)
