from pages.login_page import LoginPage


def test_quest_should_consist_word(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

