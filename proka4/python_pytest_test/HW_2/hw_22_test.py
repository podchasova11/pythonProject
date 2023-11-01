import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Selenium")


service = Service(executable_path=ChromeDriverManager().install())
wait = WebDriverWait(driver, 5, poll_frequency=1)

time.sleep(3)
driver.save_screenshot("screen.png")


class TestAddSomeBooks:

    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//button[@id='login']")
    OUTPUT_BLOCK = ("xpath", "//button[@id='login']")

    def test_fill_form_with_valid_data(self):
        driver = webdriver.Chrome(service=service)
        driver.get("https://demoqa.com/profile")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Mila11")
        assert username.get_attribute("value") == "Mila11"

        password = driver.find_element(*self.PASSWORD_FIELD)
        password.send_keys("Mila411457@")
        assert password.get_attribute("value") == "Mila411457@"

        driver.find_element(*self.LOGIN_BUTTON).click()










#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
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
#
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# class TestLogin:  # Название тестового класса
#
#     def setup(self):
#         print("Выполняюсь до теста")
#         self.service = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=self.service)
#
#     def test_open_login_page(self):
#         self.driver.get("https://demoqa.com/login")
#         login_field = self.driver.find_element("xpath", "//input[@id='userName']")
#         pytest.set_trace()  # Включаем дебаг
#         login_field.send_keys("Alexey")
#         assert login_field.get_attribute("value") == "Alexey", "Некорректный логин"
#
#     def teardown(self):
#         self.driver.close()
#         print("Выполняюсь после теста")
#