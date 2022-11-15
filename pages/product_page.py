from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Запускается для основных тестов
    def should_be_add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.solve_quiz_and_get_code()
        self.message_of_add_to_basket()
        self.include_name_of_book_in_message_of_add()
        self.message_of_cost_basket()
        self.include_cost_of_book_in_message_of_cost_basket()

    # запускается для инициализации кнопки "Добавить в корзину"
    def should_be_add_to_basket_button(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()

    # Проверка присутствия сообщение о добавлении в корзину
    def message_of_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_BASKET), 'not exist message for add basket'

    # Проверка названия вхождения названия книги в сообщение о доавблении в корзину
    def include_name_of_book_in_message_of_add(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_GOOD).text \
               == self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET).text, 'not include name of book'

    # Проверка сообщение о стоимости корзины
    def message_of_cost_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST_BASKET), 'not exist message of cost basket'

    # Проверка названия вхождения стоимости книги в сообщение о стоимости корзины
    def include_cost_of_book_in_message_of_cost_basket(self):
        assert self.browser.find_element(*ProductPageLocators.COST_OF_BOOK).text \
               == self.browser.find_element(*ProductPageLocators.MESSAGE_COST_BASKET).text, 'not include cost of book'

    # Проверка, что нет сообщение о добавлении в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_BASKET), \
            "Success message is presented, but should not be"

    # Проверка что сообщение пропадет через определенное время
    def should_not_be_Look_success_message_any_time(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_BASKET), \
            "Message is visible"
