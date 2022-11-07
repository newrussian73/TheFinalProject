from .pages.product_page import ProductPage


def quest_can_add_book_to_basket_test(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    # page.should_be_add_to_basket_button()
    # page.solve_quiz_and_get_code()
    # page.should_be_add_to_basket()
