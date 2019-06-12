from framework.base.Selenium_driver import SeleniumDriver

class MobilesAccessoriesListingPage(SeleniumDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # locators
    _redmiY2CatLink = "(//div[contains(text(),'MOBILES BY PRICE')]/../div[2]/div)[3]"
    _lenevoBrandChkbx = "//input[@name='s-ref-checkbox-Lenovo']"
    _totalExpected = "s-result-count"
    _totalActual = "//ul[@id='s-results-list-atf']/li"
    _pageNext = "pagnNextString"

    def goToRedmiY2(self):
        self.elementClick(self._redmiY2CatLink,"xpath")
        self.driver.implicitly_wait(5)
        return True
    """Method for filter by brand Lenevo"""
    def filterByBrand(self):
        self.elementClick(self._lenevoBrandChkbx,"xpath")

    """Method for get the text of total result"""
    def getTotalResultText(self):
        result = self.getElement(self._totalExpected,"id").text
        total = result.split()
        return total[2]

    """Method for get the total result from the listing"""
    def getTotalResult(self):
        allResult = self.driver.find_elements_by_xpath(self._totalActual)
        count=0
        itemCount=len(allResult)
        while itemCount!=96:
            allResult = self.driver.find_elements_by_xpath(self._totalActual)
            for item in allResult:
                count+=1
            # print("count:",count, "itemCount:", itemCount)
            if count==itemCount:
                self.elementClick(self._pageNext,"id")
            itemCount+=len(allResult)
            # print(itemCount)
        return itemCount







