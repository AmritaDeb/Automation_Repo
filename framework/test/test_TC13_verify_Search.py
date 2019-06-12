from framework.pom.HomePage import HomePage
from framework.pom.AlexaListingPage import AlexaListingPage
from framework.base.Selenium_driver import SeleniumDriver
import json
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_searchProductAlexa(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.alp = AlexaListingPage(self.driver)

    @pytest.mark.usefixtures("search","screenshot")
    def test_goToPDP(self):
        SeleniumDriver(self.driver).getMethodName(self.__class__.__name__)
        print("Successfull")
        SeleniumDriver()







