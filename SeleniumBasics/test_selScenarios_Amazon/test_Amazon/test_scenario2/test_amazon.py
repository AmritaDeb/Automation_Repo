"""
Scenario 2:
1. Open any browser.
2. Navigate to https://www.amazon.in/
3. Hover on Shop by category drop down
4. Move to Women's Fashion
5. Click on Western wear
6. Select a category from left navigation menu, say Winterwear
7. Click on Jacket under Shop by category
8. Print the total count of the result of that page
9. Print the total count of the result from all the pages
10. Click on nth product
11. Click on add to cart.
12. Verify the product is added to the cart or not.
"""

from selenium import webdriver
import time
import re
from selenium.webdriver.common.action_chains import ActionChains


class Test_Amazon:
    def test_amazon(self):
        driver=webdriver.Chrome(executable_path="D:\\TestYantra\\python\\TY\\chromedriver.exe")
        driver.get("https://www.amazon.in/")
        driver.maximize_window()
        action=ActionChains(driver)
        menu=driver.find_element_by_id("nav-link-shopall")
        action.move_to_element(menu).perform()
        submenu=driver.find_element_by_xpath("//div[@id='nav-flyout-shopAll']/div[2]//span[.=\"Women's Fashion\"]")
        action.move_to_element(submenu).perform()
        driver.find_element_by_xpath("//div[@id='nav-flyout-shopAll']/div[3]//span[.='Western Wear']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='leftNav']/ul/ul/div/li[7]/span/a/span[.='Winterwear']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='anonCarousel1']//span[.='Jackets']").click()
        time.sleep(5)
        print("The total count of that page: ", end="")
        totalCount=driver.find_elements_by_xpath("//div[@id='mainResults']/ul/li")
        print(len(totalCount))
        print("The total count of the result from all the pages: ", end="")
        total=driver.find_element_by_id("s-result-count").text
        str=total.split()
        print(str[3].replace(',',''))
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,500)")
        product1=driver.find_element_by_xpath("//div[@id='mainResults']/ul/li[1]")
        product1.click()
        time.sleep(5)

ob=Test_Amazon()
ob.test_amazon()