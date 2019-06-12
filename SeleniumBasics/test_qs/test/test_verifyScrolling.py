from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Test_VerifyScrolling:
    def test_verifyScrolling(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.get("https://www.actitime.com/license-agreement")
        driver.maximize_window()
        # driver.execute_script("window.scrollTo(0,1000)")
        # time.sleep(5)
        # driver.execute_script("window.scrollTo(0,-1000)")
        # time.sleep(5)
        for i in range(0,5):
            driver.execute_script("window.scrollTo(0, 1000);")
            time.sleep(5)
        # wait = WebDriverWait(driver, 10)
        #
        # while True:
        #     # do the scrolling
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     try:
        #         wait.until(EC.visibility_of_element_located((By.XPATH, "//*[. = 'Loading...']")))
        #     except Exception:
        #         break
