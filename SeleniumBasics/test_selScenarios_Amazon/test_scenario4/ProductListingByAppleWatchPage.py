import time
class ProductListingByAppleWatchPage:
    _resultCount="//div[@id='srp-river-results']/ul/li"
    _titleAll="//div[@id='srp-river-results']/ul/li/div/div[2]/a/h3"

    def __init__(self,driver):
        self.driver=driver

    def printResult(self):
        count=len(self.driver.find_elements_by_xpath(self._resultCount))
        print(count)

    def printNthProductTitle(self,n):
        nthProductTitle = "//div[@id='srp-river-results']/ul/li["+str(n)+"]/div/div[2]/a/h3"
        title=self.driver.find_element_by_xpath(nthProductTitle).text
        print(title)
        print("~~~~~~~~~~~~")

    def printAllProductFrom1stPage(self):
        titleAll=self.driver.find_elements_by_xpath(self._titleAll)
        for i in titleAll:
            print(i.text)
        print("~~~~~~~~~~~~~")

