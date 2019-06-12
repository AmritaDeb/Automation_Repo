"""
Scenario 3:
1. Open any browser.
2. Navigate to https://www.amazon.in/
3. Hover on Shop by category drop down
4. Move to Women's Fashion
5. Click on Western wear
6. Select a category from left navigation menu, say Winterwear
7. Click on Jacket under Shop by category
8. Filter by size, color
9. Sort the result based on price
10. print the total count of the result
11. Verify the filteration.
12. Click on nth product
13. Verify the same product is displayed or not
14. Fetch the details of the product
15. Click on add to cart and verify the product is added to the cart or not.
"""

from selenium import webdriver
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Test_Amazon:
    def test_amazon(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\TY\\chromedriver.exe")
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        action = ActionChains(driver)
        menu = driver.find_element_by_id("nav-link-shopall")
        action.move_to_element(menu).perform()
        submenu = driver.find_element_by_xpath("//div[@id='nav-flyout-shopAll']/div[2]//span[.=\"Women's Fashion\"]")
        action.move_to_element(submenu).perform()
        driver.find_element_by_xpath("//div[@id='nav-flyout-shopAll']/div[3]//span[.='Western Wear']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='leftNav']/ul/ul/div/li[7]/span/a/span[.='Winterwear']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='anonCarousel1']//span[.='Jackets']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//h4[.='Size']/..//span[.='M']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//h4[.='Colour']/..//a[@title='Red']").click()
        time.sleep(2)
        totalResult=driver.find_elements_by_xpath("//div[@id='mainResults']/ul/li//span[@class='a-size-base a-color-price s-price a-text-bold']/span")
        print("Total Result: ",totalResult)
        # for i in totalResult:
        #     print(i.text)
        sortList=driver.find_element_by_id("sort")
        select=Select(sortList)
        select.select_by_value("price-asc-rank")
        sortResult=driver.find_elements_by_xpath("//div[@id='mainResults']/ul/li//span[@class='a-size-base a-color-price s-price a-text-bold']/span")
        print("Sort Result: ",sortResult)





ob=Test_Amazon()
ob.test_amazon()
