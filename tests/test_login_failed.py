import pytest
import os
from pages.contact_page import ContactPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_invalid_credentials(driver, config):
    # Crear carpeta para capturas
    if not os.path.exists("result/assets"):
        os.makedirs("result/assets")

    contact = ContactPage(driver)

    # Intentar login con contraseña incorrecta
    contact.login(config["email"], "clave_incorrecta123")
    driver.save_screenshot("result/assets/login_failed.png")

    # Esperar a que aparezca el mensaje de error en el <body>
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Incorrect username or password")
    )

    # Verificar que el mensaje está en el HTML
    assert "Incorrect username or password" in driver.page_source
