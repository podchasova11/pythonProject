# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

#
# class TestLogin: # Название тестового класса
#
#     def setup(self, vice=None, Ser=None):
#         print("Выполняюсь до теста")
#         self.service = Ser
#         vice(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=self.service)
#
#     def test_open_login_page(self):
#         self.driver.get("https://demoqa.com/login")
#         assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"
#
#     def teardown(self):
#         self.driver.close()
#

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin:  # Название тестового класса

    def setup(self):
        print("Выполняюсь до теста")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        login_field = self.driver.find_element("xpath", "//input[@id='userName']")
        pytest.set_trace()  # Включаем дебаг
        login_field.send_keys("Alexey")
        assert login_field.get_attribute("value") == "Alexey", "Некорректный логин"

    def teardown(self):
        self.driver.close()
        print("Выполняюсь после теста")