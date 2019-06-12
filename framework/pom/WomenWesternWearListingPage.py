from framework.base.Selenium_driver import SeleniumDriver

class WomenWesternWearListingPage(SeleniumDriver):
    _winterWearLink = "//div[@id='leftNav']/ul/ul/div/li[7]/span/a/span[.='Winterwear']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def goToWinterWear(self):
        self.elementClick(self._winterWearLink,"xpath")
        self.driver.implicitly_wait(5)
        return True