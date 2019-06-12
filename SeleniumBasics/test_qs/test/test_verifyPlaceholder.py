"""
Print the background text present in the textfields.
"""
from selenium import webdriver

class Test_VerifyPlaceholder:
    def test_verifyPlaceholder(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        f_name = driver.find_element_by_name("firstname").get_attribute("placeholder")
        print(f_name)