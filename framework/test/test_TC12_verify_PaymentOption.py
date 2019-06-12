from framework.pom.HomePage import HomePage
from framework.pom.ProductDetailsPage import ProductDetailsPage
from framework.pom.ShoppingCartPage import ShoppingCartPage
from framework.pom.CartPage import CartPage
from framework.pom.AmazonLoginPage import LoginPage
from framework.pom.DeliveryAddressPage import DeliveryAddressPage
from framework.pom.ShippingOptionPage import ShippingOptionPage
from framework.pom.PaymentPage import PaymentPage
import json
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_productDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)
        self.sp = ShoppingCartPage(self.driver)
        self.cp = CartPage(self.driver)
        self.dap = DeliveryAddressPage(self.driver)
        self.sop = ShippingOptionPage(self.driver)
        self.pp = PaymentPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goToPDP(self):
        self.hp.goToLogin()
        credentials=json.loads(open('loginCredential.json').read())
        username = credentials.get('username')
        password = credentials.get('password')
        self.lp.loginAmazon(username,password)
        self.hp.goToAmazonEcho()
        self.pdp.addToCart()
        self.sp.goToCart()
        self.cp.proceedToCheckout()
        self.dap.goToAdress()
        self.sop.continueCheckout()
        self.pp.paymentDetails()






