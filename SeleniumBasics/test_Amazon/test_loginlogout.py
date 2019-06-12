from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Test_LoginLogout:
    def test_loginlogout(self):
        driver=webdriver.Chrome(executable_path="D:\TestYantra\python\selenium\chromedriver.exe")
        driver.get("https://www.amazon.in/")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        menu=driver.find_element_by_id("nav-link-yourAccount")
        ActionChains(driver).move_to_element(menu).perform()