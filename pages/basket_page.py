from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    # Проверка, есть ли товар в корзине
    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.STRING_OF_GOOD), \
            "Good in basket exist"

    # Проверка, есть ли в сообщении о пустой корзине цитата "Ваша корзина пуста"
    def should_be_text_about_empty_basket(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, \
             "basket is not empty"
