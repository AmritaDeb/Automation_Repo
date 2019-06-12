from framework.base.Selenium_driver import SeleniumDriver

class AlexaListingPage(SeleniumDriver):

    _resultKeyName = "//span[@id='s-result-count']/span/span"
    _cartId = "nav-cart-count"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    """Method for verify reuslt key name"""
    def verifyResultKeyName(self):
        return self.getElement(self._resultKeyName,"xpath").text

    """Method for go to the cart page by click on the cart link"""
    def goToCart(self):
        self.elementClick(self._cartId, "id")
        self.driver.implicitly_wait(10)
        return True


