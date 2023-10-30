from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


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
        username.send_keys("Mila")
        assert username.get_attribute("value") == "Mila"

        email = driver.find_element(*self.EMAIL_FIELD)
        email.send_keys("pod@ya.ru")
        assert email.get_attribute("value") == "pod@ya.ru"

        address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
        address.send_keys("Kirova 27")
        assert address.get_attribute("value") == "Kirova 27"

        driver.find_element(*self.SUBMIT_BUTTON).click()

        output = driver.find_element(*self.OUTPUT_BLOCK)
        assert output.is_displayed() is True
        assert ("Mila" and "pod@ya.ru" and "Kirova 27") in output.text