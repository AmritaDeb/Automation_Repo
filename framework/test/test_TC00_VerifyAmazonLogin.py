from framework.pom.HomePage import HomePage
from framework.pom.AmazonLoginPage import LoginPage
import pytest
import unittest
import json

@pytest.mark.usefixtures("oneTimeSetUp", "setUp", "loginLogout")
class Test_login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp, loginLogout):
        self.hp = HomePage(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.hp.verifyLoggedinUser()
        self.hp.goToCart()
        print("I am in cart")


