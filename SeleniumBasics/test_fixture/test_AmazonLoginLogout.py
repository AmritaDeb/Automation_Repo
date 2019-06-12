from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import time

class Test_AmazonLaunch:
    @pytest.fixture()
    def launch(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://www.amazon.in/")
        driver.maximize_window()

        action = ActionChains(driver)
        signInLink = driver.find_element_by_id("nav-link-yourAccount")
        action.move_to_element(signInLink).perform()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='nav-flyout-ya-signin']//span[.='Sign in']").click()
        time.sleep(5)
        driver.find_element_by_id("ap_email").send_keys("8910945599")
        driver.find_element_by_id("continue").click()
        time.sleep(5)
        driver.find_element_by_id("ap_password").send_keys("amazon")
        driver.find_element_by_id("signInSubmit").click()

        yield driver
        signOutLink = driver.find_element_by_id("nav-link-yourAccount")
        action.move_to_element(signOutLink).perform()
        time.sleep(5)
        driver.find_element_by_id("nav-item-signout").click()
        driver.close()

    def test_amazonPurchase(self,launch):
        driver.find_element_by_id("nav-cart").click()



