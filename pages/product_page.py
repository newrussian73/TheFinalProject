from base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.message_of_add_to_basket()
        self.include_name_of_book_in_message_of_add()
        self.message_of_cost_basket()
        self.include_cost_of_book_in_message_of_cost_basket()

    def should_be_add_to_basket_button(self):
        self.browser.find_element(ProductPageLocators.ADD_TO_BASKET).click()

    def message_of_add_to_basket(self):
        assert self.is_element_present(ProductPageLocators.MESSAGE_ADD_BASKET), 'not exist message for add basket'

    def include_name_of_book_in_message_of_add(self):
        assert self.browser.find_element(ProductPageLocators.NAME_OF_GOOD).text \
               in self.browser.find_element(ProductPageLocators.MESSAGE_ADD_BASKET).text, 'not include name of book'

    def message_of_cost_basket(self):
        assert self.is_element_present(ProductPageLocators.MESSAGE_COST_BASKET), 'not exist message of cost basket'

    def include_cost_of_book_in_message_of_cost_basket(self):
        assert self.browser.find_element(ProductPageLocators.COST_OF_BOOK).text \
               in self.browser.find_element(ProductPageLocators.MESSAGE_COST_BASKET).text, 'not include cost of book'
