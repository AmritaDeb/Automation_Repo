import time
class WomenWesternWearPage:
    _winterWearLink="//div[@id='leftNav']/ul/ul/div/li[7]/span/a/span[.='Winterwear']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnWinterWear(self):
        self.driver.find_element_by_xpath(self._winterWearLink).click()
        time.sleep(2)