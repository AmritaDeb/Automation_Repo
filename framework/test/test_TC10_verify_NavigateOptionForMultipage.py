from framework.pom.HomePage import HomePage
from framework.pom.MobilesAccessoriesListingPage import MobilesAccessoriesListingPage
from framework.pom.RedmiListingPage import RedmiListingPage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_productDetails(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.mlp = MobilesAccessoriesListingPage(self.driver)
        self.rlp = RedmiListingPage(self.driver)

    @pytest.mark.run(order=1)
    def test_goToPDP(self):
        self.hp.goToMobilePhones()
        self.mlp.goToRedmiY2()
        self.rlp.filterByOSColor()
        self.rlp.navigateToMultipage()





