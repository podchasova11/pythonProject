import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # ('Open a browser')
    def open(self):
        self.driver.get(self.url)

    # ('Find a visible element')
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # ('Find visible elements')
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # ('Find a present element')
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # ('Find present elements')
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # ('Find a not visible element')
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    # ('Find clickable elements')
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, param):
        pass

    @pytest.fixture()
    def connect_data_base(self):
        connection = sqlite3.connect("test.db")
        print("Мы подключили ДБ")
        return connection

    @pytest.fixture()
    def generate_data_way_2(request):
        login = f"autotest_{time.time()}@ya.ru"
        password = "123"
        request.cls.login = login
        request.cls.password = password

