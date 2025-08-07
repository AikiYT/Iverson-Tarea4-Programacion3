import pytest
import os
from pages.contact_page import ContactPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_contact_with_short_phone(driver, config):
    # Crear carpeta si no existe
    if not os.path.exists("result/assets"):
        os.makedirs("result/assets")

    contact = ContactPage(driver)

    # Hacer login
    contact.login(config["email"], config["password"])
    driver.save_screenshot("result/assets/login_limit_login.png")

    # Intentar crear contacto con número de teléfono muy corto
    contact.add_contact("Limite", "Prueba", "12")  # Teléfono inválido (demasiado corto)
    driver.save_screenshot("result/assets/phone_limit_test.png")

    # Verificar que el contacto NO se agregó, esperando que no redirija a "My Contacts"
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "submit"))
    )

    # Asegurar que seguimos en la vista de formulario (no se aceptó)
    assert "Add Contact" in driver.title