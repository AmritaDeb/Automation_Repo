from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains


class DeliveryAddressPage(SeleniumDriver):

    _saveAddressLink="//a[contains(text(),'Deliver to this address')]"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    """Method for proceed to delivery address"""
    def goToAdress(self):
        self.elementClick(self._saveAddressLink,"xpath")
        self.driver.implicitly_wait(5)
        return True
