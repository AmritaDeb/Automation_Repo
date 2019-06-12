from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class CartPage(SeleniumDriver):
    _checkoutName = "proceedToCheckout"
    _totalAmount = "//span[@id='sc-subtotal-amount-activecart']/span/span"
    _quantity = "//span[@class='a-dropdown-prompt']"
    _deleteProduct = "//form[@id='activeCartViewForm']//input[@value='Delete']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    """Method for proceed to checkout from cart page"""
    def proceedToCheckout(self):
        self.elementClick(self._checkoutName,"name")
        self.driver.implicitly_wait(10)
        return True
    """Method for get the quantity of items added in cart"""
    def getTheQuantity(self):
        quantity=self.getElement(self._quantity,"xpath").text
        return quantity
    """Method for get the total amount of cart"""
    def getTheTotalAmount(self):
        total=self.getElement(self._totalAmount,"xpath").text
        return total
    """Method for removing items from cart one by one"""
    def removeProduct(self):
        allProduct=self.driver.find_elements_by_xpath(self._deleteProduct)
        for product in allProduct:
            product.click()

