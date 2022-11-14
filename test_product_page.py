from .pages.product_page import ProductPage
import pytest


# @pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer0", marks=pytest.mark.xfail(reason="1")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer1", marks=pytest.mark.xfail(reason="2")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer2", marks=pytest.mark.xfail(reason="3")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer3", marks=pytest.mark.xfail(reason="4")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer4", marks=pytest.mark.xfail(reason="5")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer5", marks=pytest.mark.xfail(reason="6")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer6", marks=pytest.mark.xfail(reason="7")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer7", marks=pytest.mark.xfail(reason="8")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer8", marks=pytest.mark.xfail(reason="9")),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer9", marks=pytest.mark.xfail(reason="10"))])
# def test_quest_can_add_book_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket()


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link_other = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link_other)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_guest_cant_see_success_message(browser):
    link_other = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link_other)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    link_other = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link_other)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_not_be_Look_success_message_any_time()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    link_ti = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link_ti)
    page.open()
    page.go_to_login_page()
