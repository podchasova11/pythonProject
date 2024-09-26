Class BasePage():

@HandleExcElementsDecorator()
    def current_page_is(self, link):
        print(f"{datetime.now()}   current_page = {self.driver.current_url}")
        print(f"{datetime.now()}   link = {link}")
        return link == self.driver.current_url

def current_page_is(self,link):
    return link == self.driver.current_url

def current_page_is(self,link):
    return link == salf.driver.current_url

# self - ссылка на текущий экземпляр класса

_______________________

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

# init — это специальная функция, которая вызывается при создании нового
# объекта класса. Она также известна как конструктор класса. Это место, где
# обычно устанавливаются начальные значения атрибутов класса.
# В примере выше, init принимает три аргумента: self, color и brand. 
# color и brand — это значения, которые передаются при создании нового объекта класса Car,
# и они устанавливаются в качестве атрибутов объекта.

# self - ссылка на текущий экземпляр класса

____________________________________________
