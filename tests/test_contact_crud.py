import os
from pages.contact_page import ContactPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_and_add_contact(driver, config):
    if not os.path.exists("result/assets"):
        os.makedirs("result/assets")

    contact = ContactPage(driver)

    # Hacer login
    contact.login(config["email"], config["password"])
    driver.save_screenshot("result/assets/login_success.png")

    # Agregar contacto
    contact.add_contact("Juan", "Perez", "8291234567")
    driver.save_screenshot("result/assets/contact_added.png")

    # Esperar que el contacto aparezca en la tabla
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table//td[contains(text(), 'Juan')]"))
    )

    assert "Juan" in driver.page_source



