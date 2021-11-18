#TODO разобраться с WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
#TODO разобраться с expected_conditions
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        # В классе BasePage создаем конструктор, который принимает driver — экземпляр webdriver. Указываем base_url, который будет использоваться для открытия страницы.
        self.driver = driver
        self.base_url = "https://www.labirint.ru/"

    # Далее создаем методы find_element (ищет один элемент и возвращает его) и find_elements (ищет множество и возвращает в виде списка)
    def find_element(self, locator, time=10):
        # time=10 - значение по умолчанию. Обозначено, чтобы человек мог передать на вход любое другое значение.
        # until - функция, которая принимает на вход метод и сообщение об ошибке
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url
