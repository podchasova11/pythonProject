from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestLogin: # Название тестового класса

    def test_open_login_page(self): # Название теста
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.saucedemo.com/")
        assert driver.current_url == "https://www.saucedemo.com/", "Открыта некорректная страница"