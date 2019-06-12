from framework.base.Selenium_driver import SeleniumDriver

class WinterWearListingPage(SeleniumDriver):
    _product1 = "//div[@id='mainResults']/ul/li[1]"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def goTo1stProduct(self):
        self.elementClick(self._product1,"xpath")
        self.driver.implicitly_wait(5)
        return True
