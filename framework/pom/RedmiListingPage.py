from builtins import print

from framework.base.Selenium_driver import SeleniumDriver
import re

class RedmiListingPage(SeleniumDriver):
    _totalCount = "s-result-count"
    _products = "//ul[@id='s-results-list-atf']/li//h2"
    _pageNext = "pagnNextString"
    _chkbxAndroid = "//h4[.='Operating System']/following-sibling::ul[1]/div/li[1]"
    _filterBlack = "//h4[.='Colour']/following-sibling::ul[2]//span[.='Black']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    """Method for filteration by OS (Android) & Color (Black)"""
    def filterByOSColor(self):
        self.elementClick(self._chkbxAndroid,"xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._filterBlack, "xpath")
        self.driver.implicitly_wait(5)

    def navigateToMultipage(self):
        next = self.getElement(self._pageNext,"id")
        while next.is_enabled():
            next.click()

    """Method for fetch the text of total count of the result from top of the listings"""
    def totalResultExpected(self):
        result = self.getElement(self._totalCount).text
        count = result.split()
        total = int(re.sub(r"[^\d.]", "", count[2]))
        return total

    # def goToNextPage(self):
    #     self.elementClick(self._pageNext,"id")
    #     self.driver.implicitly_wait(5)
    #     return True

    """Method for fetch the actual count of the result by performing pagination"""
    def resultActual(self):
        allInPage = self.driver.find_elements_by_xpath(self._products)
        actual=[]
        # temp = len(allInPage)
        pageCount = len(allInPage)
        while pageCount != self.totalResultExpected():
            print(pageCount)
            allInPage = self.driver.find_elements_by_xpath(self._products)
            for i in range(len(allInPage)):
            # if len(actual)<=len(allInPage):
                for item in allInPage:
                    actual.append(item.text)
            else:
                self.elementClick(self._pageNext,"id")
            pageCount+=len(allInPage)
        self.driver.implicitly_wait(5)
        print(len(actual))
        return True


