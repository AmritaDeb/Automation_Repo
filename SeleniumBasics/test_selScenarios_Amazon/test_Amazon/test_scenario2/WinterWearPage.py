import time

class WinterWearPage:
    _jacketCatLink="//div[@id='anonCarousel1']//span[.='Jackets']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnJacket(self):
        self.driver.find_element_by_xpath(self._jacketCatLink).click()
        time.sleep(2)