import pytest
from selenium import webdriver


# TODO погуглить yield, назначение данной фикстуры
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    # Далее используем конструкцию yield, которая разделяет функцию на часть — до тестов и после тестов.
    yield driver
    # В части “после тестов” мы вызываем функцию quit, которая завершает сессию и убивает экземпляр webdriver.
    driver.quit()
