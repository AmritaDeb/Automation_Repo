import time
class WomenJacketPage:
    _mainResults="//div[@id='mainResults']/ul/li"
    _totalCount="s-result-count"
    _product1="//div[@id='mainResults']/ul/li[1]"

    def __init__(self,driver):
        self.driver=driver

    def printTotalCount(self):
        print("The total count of that page: ", end="")
        totalCount=self.driver.find_element_by_xpath(self._mainResults)
        print(len(totalCount))
        print("The total count of the result from all the pages: ", end="")
        total=self.driver.find_element_by_id(self._totalCount).text
        str = total.split()
        print(str[3].replace(',', ''))
        time.sleep(5)
    def clickOn1stProduct(self):
        self.driver.find_element_by_xpath(self._product1).click()

