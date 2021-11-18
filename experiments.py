from BasePage import BasePage
from LabirintPages import SearchHelper
from selenium.webdriver.common.by import By
import re
from selenium import webdriver


class LabirintSeacrhLocators:
    LOCATOR_LABIRINT_SEARCH_FIELD = (By.ID, "search-field")
    LOCATOR_LABIRINT_SEARCH_BUTTON = (By.CLASS_NAME, "b-header-b-search-e-btn")
    LOCATOR_LABIRINT_SEARCH_RESULT_MESSAGE = (By.CLASS_NAME, "index-top-title")

class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        # Передаем время - 2 секунды. Можно опустить параметр.
        return self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_BUTTON, time=2).click()

    def check_result_info_message(self):
        message = self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_RESULT_MESSAGE, time=2).get_attribute(
            "textContent")
        new_message = self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_RESULT_MESSAGE,
                                    time=2).text
        # Заменяем 2 и более пробела на 1 пробел и убираем пробел в конце.
        return message, new_message


def labirint_search_check_final_page():
    word = 'Кот'
    driver = webdriver.Chrome(executable_path="./chromedriver")
    search_labirint = SearchHelper(driver)
    search_labirint.go_to_site()
    search_labirint.enter_word(word)
    search_labirint.click_on_the_search_button()
    message, new_message = search_labirint.check_result_info_message()
    print (message, new_message)


labirint_search_check_final_page()

