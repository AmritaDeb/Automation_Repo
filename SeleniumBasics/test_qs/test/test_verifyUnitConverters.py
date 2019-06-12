"""
Automate following scenario, go to UnitConverters.net website, enter 100 from textbox,
get the value present in a 'to' textbox and printed
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Test_VerifyUnitConverters:
    def test_verifyUnitConverters(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://www.unitconverters.net/")
        driver.maximize_window()
        from_list = driver.find_element_by_id("calFrom")
        from_select = Select(from_list)
        options = from_select.options
        for option in options:
            print(option.text)
        from_select.select_by_value("2")
        driver.find_element_by_name("fromVal").send_keys("100")
        time.sleep(5)
        to_list = driver.find_element_by_id("calTo")
        to_select = Select(to_list)
        to_select.select_by_value("1")
        print(driver.find_element_by_name("toVal").get_attribute("value"))
        time.sleep(6)
