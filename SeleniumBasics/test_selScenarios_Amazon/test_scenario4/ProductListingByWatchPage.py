import time
class ProductListingByWatchPage:
    _searchField="//input[@placeholder='Search for anything']"
    _searchBtn="//input[@value='Search']"
    def __init__(self,driver):
        self.driver=driver

    def search(self,keyword):
        self.driver.find_element_by_xpath(self._searchField).send_keys(keyword)
        time.sleep(5)
        self.driver.find_element_by_xpath(self._searchBtn).click()