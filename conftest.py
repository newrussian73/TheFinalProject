from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from webdriver_manager.chrome import ChromeDriverManager



def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help='Choose browser: firefox or chrome')
    parser.addoption("--language", action='store', default='en', help='Choose language')
    parser.addoption("--executor", action="store", default="192.168.1.252")
    parser.addoption("--url", action="store", default='http://192.168.1.252:8081')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    executor = request.config.getoption("--executor")
    if executor == "local":
        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            print('\nstart browser for test..')
            browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        elif browser_name == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference('intl.accept_languages', language)
            print('\nstart browser for test..')
            browser = webdriver.Firefox(firefox_profile=fp)
            yield browser
            print('\nquit browser..')
            browser.quit()
    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browser_name": browser_name
        }


