from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:
    _shopByCaIid="nav-link-shopall"
    _submenu="//div[@id='nav-flyout-shopAll']/div[2]//span[.=\"Women's Fashion\"]"
    _subCatLink="//div[@id='nav-flyout-shopAll']/div[3]//span[.='Western Wear']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnWesternWear(self):
        action=ActionChains(self.driver)
        menu=self.driver.find_element_by_id(self._shopByCaIid)
        action.move_to_element(menu).perform()
        time.sleep(2)
        submenu=self.driver.find_element_by_xpath(self._submenu)
        action.move_to_element(submenu).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self._subCatLink).click()
        time.sleep(2)
