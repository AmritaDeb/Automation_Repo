from framework.pom.HomePage import HomePage
from framework.pom.WomenWesternWearListingPage import WomenWesternWearListingPage
from framework.pom.WinterWearListingPage import WinterWearListingPage
from framework.pom.ProductDetailsPage import ProductDetailsPage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_productDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.wlp = WomenWesternWearListingPage(self.driver)
        self.wwlp = WinterWearListingPage(self.driver)
        self.pdp = ProductDetailsPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goToPDP(self):
        self.hp.goToWesternWear()
        self.wlp.goToWinterWear()
        self.wwlp.goTo1stProduct()
        # self.pdp.selectSize()
        # print(self.pdp.getAvailibility())
        # self.pdp.addToCart()


