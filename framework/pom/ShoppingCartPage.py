from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class ShoppingCartPage(SeleniumDriver):

    _cartId="nav-cart-count"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def goToCart(self):
        self.elementClick(self._cartId,"id")
        self.driver.implicitly_wait(10)
        return True

    def proceedToCheckout(self):
        self.elementClick(self._checkout,"xpath")
        self.driver.implicitly_wait(10)
        return True



