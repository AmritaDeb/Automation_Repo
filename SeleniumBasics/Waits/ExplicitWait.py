from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_VerifyLogin:
    @pytest.fixture()
    def launch(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://www.gmail.com")
        driver.maximize_window()
        yield driver
        driver.close()
    def test_verifyLogin(self,launch):
        driver.find_element_by_id("identifierId").send_keys("amrita.d@testyantra.com")
        driver.find_element_by_xpath("//span[.='Next']").click()
        time.sleep(10)
        try:
            ele_pw = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"password")))
            ele_pw.send_keys("amrita_ty@2018")
        finally:
            # driver.find_element_by_name("password").send_keys("amrita_ty@2018")
            driver.find_element_by_xpath("//span[.='Next']").click()
        try:
            inbox_count = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//a[.='Inbox']/../following-sibling::div")))
            print(inbox_count.text)
            # inbox_count = driver.find_element_by_xpath("//a[.='Inbox']/../following-sibling::div").text
        finally:
            return


