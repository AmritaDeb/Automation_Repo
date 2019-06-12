import pytest
from framework.base.Extended_Webdriver import Extended_Webdriver
from framework.base.Selenium_driver import SeleniumDriver
from framework.pom.AmazonLoginPage import LoginPage
from framework.pom.HomePage import HomePage
from framework.pom.AlexaListingPage import AlexaListingPage
import json

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    EW = Extended_Webdriver(browser)
    driver = EW.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

"""fixture for login and logout"""
@pytest.fixture(scope="class")
def loginLogout(request):
    hp = HomePage(request.cls.driver)
    lp = LoginPage(request.cls.driver)

    credentials = hp.fetchJSONData('loginCredential.json')
    username = credentials.get('username')
    password = credentials.get('password')

    hp.goToLogin()
    lp.loginAmazon(username,password)
    print("Successfully login")

    yield
    hp.logout()
    print("Successfully logout")

"""fixture for sesrch the product """
@pytest.fixture(scope="function")
def search(request):
    key = "alexa"
    hp = HomePage(request.cls.driver)
    alp = AlexaListingPage(request.cls.driver)
    hp.searchProduct(key)
    yield
    print("Searching validated")
    assert key in alp.verifyResultKeyName(),"Result products are not matched with the search key"
    print("Result products are matched with the search key")

@pytest.fixture(scope="function")
def screenshot(request):
    hp = HomePage(request.cls.driver)
    # SeleniumDriver(request.cls.driver).takeScreenshot()
    yield
    SeleniumDriver(request.cls.driver).takeScreenshot()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")