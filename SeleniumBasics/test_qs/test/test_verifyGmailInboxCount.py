from selenium import webdriver
from SeleniumBasics.test_qs.pom.LoginPage import LoginPage
import pytest
import time

class Test_VerifyLogin:
    @pytest.fixture()
    def launch(self):
        # global driver
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://www.gmail.com")
        driver.maximize_window()
        self.lp = LoginPage(driver)
        yield
        driver.close()
    def test_verifyLogin(self,launch):
        self.lp.clickLogin("amrita.d@testyantra.com","amrita_ty@2018")
        inboxCount = int(self.lp.fetchInboxCount())
        assert inboxCount > 0, "No mail found"


