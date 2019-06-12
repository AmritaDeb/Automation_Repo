from selenium import webdriver
import datetime

class Test_Screenshot2:
    def test_screenshot(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://google.com")
        driver.maximize_window()
        name = self.__class__.__name__
        print(name)
        datetime_now = datetime.datetime.now()
        print(datetime_now)
        current = datetime_now.strftime("%m_%d_%Y_%H_%M_%S")
        print(current)

        driver.get_screenshot_as_file("photo/"+name+"_"+current+".png")

