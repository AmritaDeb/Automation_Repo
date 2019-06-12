from selenium import webdriver
import pytest
import time

class Test_VerifyLogin:
    @pytest.fixture()
    def launch(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://www.gmail.com")
        driver.maximize_window()
        yield driver
        driver.close()
        # self.driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        # self.driver.get("https://www.gmail.com")
        # self.driver.maximize_window()
        # yield self.driver
        # self.driver.close()
    def test_verifyLogin(self,launch):
        launch.find_element_by_id("identifierId").send_keys("**********")
        launch.find_element_by_xpath("//span[.='Next']").click()
        time.sleep(10)
        launch.find_element_by_name("password").send_keys("*********")
        launch.find_element_by_xpath("//span[.='Next']").click()
        time.sleep(10)
        inbox_count = launch.find_element_by_xpath("//a[.='Inbox']/../following-sibling::div").text
        print(inbox_count)
        # un = self.driver.find_element_by_id("identifierId")
        # un.send_keys("***********")
        # self.driver.find_element_by_xpath("//span[.='Next']").click()
        # time.sleep(10)
        # self.driver.find_element_by_name("password").send_keys("**********")
        # self.driver.find_element_by_xpath("//span[.='Next']").click()
        # time.sleep(10)
        # inbox_count = self.driver.find_element_by_xpath("//a[.='Inbox']/../following-sibling::div").text
        # print(inbox_count)



