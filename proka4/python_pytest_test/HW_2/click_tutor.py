from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://qa-playground.com/")
sign_in_button = driver.find_element("xpath", "//a[text()='Sign in']")
sign_in_button.click()