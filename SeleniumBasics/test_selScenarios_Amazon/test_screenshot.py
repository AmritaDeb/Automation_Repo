from selenium import webdriver
import time

class Test_Screenshot:
    def test_screenshot(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://demo.actitime.com/login.do")
        driver.maximize_window()
        driver.get_screenshot_as_file("photo/login2.png")


