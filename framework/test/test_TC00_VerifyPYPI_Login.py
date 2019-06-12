from framework.pom.LoginPage import LoginPage
import pytest
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Test_login(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.goToLoginPage()
        self.lp.LoginPYPI("anupsahoo", "admin@#$%")

    @pytest.mark.run(order=2)
    def test_verifyLoginPage(self):
        assert self.lp.verify_login_successful()

    # def test_go_to_AccountSetting(self):
    #     assert self.lp.gotoAccountSetting()

    @pytest.mark.run(order=3)
    def test_goToInstallpackagePage(self):
        self.lp.goToInstallingpackage()


    @pytest.mark.run(order=4)
    def test_goToUploadPackage(self):
        self.lp.goToUploadPackage()
