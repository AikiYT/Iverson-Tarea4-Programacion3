from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).clear()
        self.find(by, value).send_keys(text)
