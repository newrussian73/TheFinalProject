from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from os import getenv

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help='Choose browser: firefox or chrome')
    parser.addoption("--language", action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print('\nstart browser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        print('\nstart browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print('\nquit browser..')
    browser.quit()
