from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class ProductDetailsPage(SeleniumDriver):
    _availibilityAlexa = "//div[@id='availability']/span"
    _reviewCountAlexa = "//div[@id='averageCustomerReviews_feature_div']/div/span/a"
    _reviewAlexa="//div[@id='cm-cr-dp-review-list']//a[@data-hook='review-title']"
    _titleAlexa="productTitle"
    _availibility = "//h2[.='Product details']/../div/ul/li[3]/b"
    _sizeID = "native_dropdown_selected_size_name"
    _reviewId="acrCustomerReviewText"
    _addToCartId="add-to-cart-button"
    _cartId = "nav-cart-count"
    # _addToCart="//span[@id='submit.add-to-cart']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def getTitleAlexa(self):
        title=self.getElement(self._titleAlexa,"id").text
        return title

    def getAvailibilityAlexa(self):
        availibility=self.getElement(self._availibilityAlexa,"xpath").text
        return availibility

    def getReviewCount(self):
        review=self.getElement(self._reviewCountAlexa,"xpath").text
        count=review.split()
        return count[0]

    def getReviews(self):
        allreview=self.driver.find_elements_by_xpath(self._reviewAlexa)
        list=['bad','worst']
        posReviewCount=0
        negReviewCount=0
        for review in allreview:
            if review.text in list:
                negReviewCount+=1
            else:
                posReviewCount+=1
        print("the positive review: ", posReviewCount)
        print("the negetive review: ", negReviewCount)

    def addToCart(self):
        self.elementClick(self._addToCartId,"id")
        self.driver.implicitly_wait(5)
        return True

    def goToCart(self):
        self.elementClick(self._cartId,"id")
        self.driver.implicitly_wait(10)
        return True

    # def getAvailibility(self):
    #     availibility=self.getElement(self._availibility,"xpath").text
    #     # print(self.driver.find_element_by_xpath(self._availibility).text)
    #     return availibility

    # def selectSize(self):
    #     size=self.getElement(self._sizeID,"id")
    #     select=Select(size)
    #     option=select.select_by_index(3)
    #     self.driver.implicitly_wait(5)
    #



