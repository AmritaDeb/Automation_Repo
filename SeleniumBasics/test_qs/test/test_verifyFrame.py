from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Test_VerifyFrame:
    def test_verifyFrame(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("http://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(0)
        drag = driver.find_element_by_id("draggable")
        drop = driver.find_element_by_id("droppable")
        action = ActionChains(driver)
        action.drag_and_drop(drag,drop).perform()
        time.sleep(3)

