import os
from selenium.webdriver.common.by import By
from pages.contact_page import ContactPage

def test_phone_too_short(driver, config):
    if not os.path.exists("result/assets"):
        os.makedirs("result/assets")

    contact = ContactPage(driver)
    contact.login(config["email"], config["password"])
    driver.save_screenshot("result/assets/short_phone_login.png")

    contact.add_contact("Corto", "Numero", "123")
    driver.save_screenshot("result/assets/short_phone_attempt.png")

    # Validamos que estamos en la página de creación (no redirige)
    assert driver.title == "Add Contact"
    assert "Corto Numero" not in driver.page_source



