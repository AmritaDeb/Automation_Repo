from selenium import webdriver
import time

class Test_VerifyWindowHandle:
    def test_verifyWindowHandle(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://demo.automationtesting.in/Windows.html")
        driver.find_element_by_xpath("//div[@id='Tabbed']/a/button[contains(text(),'click')]").click()
        parent = driver.current_window_handle
        print(driver.title)
        handles = driver.window_handles
        handles.remove(parent)
        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.title)
            # if driver.title == "Frames & windows":
            #     driver.close()