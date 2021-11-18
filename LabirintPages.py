from BasePage import BasePage
# TODO узнать, в чем суть BY
# Помимо общедоступных (public) методов, перечисленных выше, существует два приватных (private) метода,
# которые при знании указателей объектов страницы могут быть очень полезны: find_element and find_elements.
from selenium.webdriver.common.by import By
import re


class LabirintSeacrhLocators:
    # TODO уточнить, что за магия происходит под капотом
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
        message = self.find_element(LabirintSeacrhLocators.LOCATOR_LABIRINT_SEARCH_RESULT_MESSAGE, time=2).get_attribute("innerHTML")
        # Заменяем 2 и более пробела на 1 пробел и убираем пробел в конце.
        message = (re.sub("\s{2,}", " ", message)).rstrip(" ")
        return message

    def check_current_url(self):
        current_url = self.get_current_url()
        return current_url
