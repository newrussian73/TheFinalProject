from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest



def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome', help='Choose browser: firefox or chrome')
    parser.addoption("--language", action='store', default='en', help='Choose language')
    parser.addoption("--executor", action="store", default="local")


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
            browser = webdriver.Chrome(options=options)
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
        print('\nquit browser..')
        options = Options()
        browser = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps,
            options=options
        )
        yield browser
        browser.quit()




