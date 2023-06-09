import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")
    if browser == "chrome":                                                                     #it choses between Chrome or Firefox
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
                                                                                                # implicity wait    
    #my_driver.implicitly_wait(3)
    yield my_driver
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )