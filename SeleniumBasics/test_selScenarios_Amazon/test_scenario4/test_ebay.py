"""
Scenario 4:
1. Open any Browser of your choice (Mozilla firefox, Chrome, Internet Explorer or Safari). Write the
code in such way that based on argument passed respective browser is selected.
2. Browse to Ebay website.
3. Write a method which do following:
4. On the homepage, there is a search box, type some product (say Apple Watches).
5. From categories dropdown, select the category of your product (say Watches).
6. Click Search button.
"""

from selenium import webdriver
import time
from test_selScenarios.test_scenario4.Base import Base
from test_selScenarios.test_scenario4.HomePage import HomePage
from test_selScenarios.test_scenario4.ProductListingByWatchPage import ProductListingByWatchPage
from test_selScenarios.test_scenario4.ProductListingByAppleWatchPage import ProductListingByAppleWatchPage

class Test_Ebay:
    def test_ebay(self):
        driver=Base.launchBrowser(self,"Chrome")
        driver.get("https://www.ebay.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hp=HomePage(driver)
        hp.shopByCat()
        pl=ProductListingByWatchPage(driver)
        pl.search('Apple Watches')
        pla=ProductListingByAppleWatchPage(driver)
        pla.printResult()
        pla.printNthProductTitle(10)
        pla.printAllProductFrom1stPage()

ob=Test_Ebay()
ob.test_ebay()
