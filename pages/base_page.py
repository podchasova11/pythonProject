from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __int__(self, driver, url='https://demoqa.com'):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(self))

    def go_to_element(self, element):      # 'Go to specified element'
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_present(self, locator, timeout=5):   # 'Find a present element'
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        
