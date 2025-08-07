import yaml
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def config():
    with open("data/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def driver(config):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(config["url"])
    yield driver
    driver.quit()
