from LabirintPages import SearchHelper
import allure
# TODO узнать, что такое AttachmentType
from allure_commons.types import AttachmentType


@allure.feature('Search field')
@allure.story('Позитивный кейс: поиск с ключевым словом')
@allure.severity('critical')
def test_labirint_search_check_final_page(browser):
    word = 'Кот'
    # TODO зачем дважды мы передаем фикстуру?
    search_labirint = SearchHelper(browser)
    search_labirint.go_to_site()
    search_labirint.enter_word(word)
    search_labirint.click_on_the_search_button()
    message = search_labirint.check_result_info_message()
    assert message == f"Все, что мы нашли в Лабиринте по запросу «{word}»"


@allure.feature('Search field')
@allure.story('Позитивный кейс: поиск с ключевым словом')
@allure.severity('critical')
def test_current_url_after_search(browser):
    word = 'Кот'
    search_labirint = SearchHelper(browser)
    search_labirint.go_to_site()
    search_labirint.enter_word(word)
    search_labirint.click_on_the_search_button()
    current_url = search_labirint.get_current_url()
    assert "https://www.labirint.ru/search/" in current_url


@allure.feature('Search field')
@allure.story('Негативный кейс: нажатие на кнопку поиска с пустым полем ввода')
@allure.severity('trivial')
def test_check_search_button_with_empty_field(browser):
    search_labirint = SearchHelper(browser)
    search_labirint.go_to_site()
    search_labirint.click_on_the_search_button()
    current_url = search_labirint.get_current_url()
    assert current_url == "https://www.labirint.ru/"