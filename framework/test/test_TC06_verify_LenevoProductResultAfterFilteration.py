from framework.pom.HomePage import HomePage
from framework.pom.MobilesAccessoriesListingPage import MobilesAccessoriesListingPage
from framework.pom.RedmiListingPage import RedmiListingPage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_productListing(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.mlp = MobilesAccessoriesListingPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goToPDP(self):
        self.hp.goToMobilePhones()
        self.mlp.filterByBrand()
        expected = self.mlp.getTotalResultText()
        actual = self.mlp.getTotalResult()
        print(expected,actual)





