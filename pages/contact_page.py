from selenium.webdriver.common.by import By
from .base_page import BasePage
from data.locators import LoginLocators, ContactLocators

class ContactPage(BasePage):
    def login(self, email, password):
        self.type(By.ID, LoginLocators.EMAIL, email)
        self.type(By.ID, LoginLocators.PASSWORD, password)
        self.click(By.ID, LoginLocators.SUBMIT)

    def add_contact(self, name, lastname, phone):
        self.click(By.ID, ContactLocators.ADD_BUTTON)
        self.type(By.ID, ContactLocators.NAME_INPUT, name)
        self.type(By.ID, ContactLocators.LASTNAME_INPUT, lastname)
        self.type(By.ID, ContactLocators.PHONE_INPUT, phone)
        self.click(By.ID, ContactLocators.SUBMIT_BUTTON)
