from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestLogin: # Название тестового класса

    def test_open_login_page(self): # Название теста
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://demoqa.com/login")
        assert driver.current_url == "https://demoqa.com/login", "Открыта некорректная страница"


class TestExample:

    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    OUTPUT_BLOCK = ("xpath", "//div[@id='output']")

    def test_fill_form_with_valid_data(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Aleksei")
        assert username.get_attribute("value") == "Aleksei"

        email = driver.find_element(*self.EMAIL_FIELD)
        email.send_keys("mani@ya.ru")
        assert email.get_attribute("value") == "mani@ya.ru"

        address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
        address.send_keys("Chapaeva 23")
        assert address.get_attribute("value") == "Chapaeva 23"

        driver.find_element(*self.SUBMIT_BUTTON).click()

        output = driver.find_element(*self.OUTPUT_BLOCK)
        assert output.is_displayed() is True
        assert ("Aleksei" and "mani@ya.ru" and "Chapaeva 23") in output.text