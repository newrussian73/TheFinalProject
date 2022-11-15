from .pages.basket_page import BasketPage
import pytest


@pytest.mark.new()
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_goods_in_basket()
    page.should_be_text_about_empty_basket()
