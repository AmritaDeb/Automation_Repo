from selenium.webdriver.common.action_chains import ActionChains
import time
class HomePage:
    _catDropDown="//button[.='Shop by category']"
    _watchLink="//h2[.='Shop by category']/..//a[.='Watches']"

    def __init__(self,driver):
        self.driver=driver

    def shopByCat(self):
        # action = ActionChains(self.driver)
        # catDropDown=self.driver.find_element_by_xpath(self._catDropDown)
        # action.move_to_element(catDropDown).perform()
        self.driver.find_element_by_xpath(self._catDropDown).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self._watchLink).click()
