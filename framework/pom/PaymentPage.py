from framework.base.Selenium_driver import SeleniumDriver
from selenium.webdriver.support.ui import Select

class PaymentPage(SeleniumDriver):
    _defaultPaymentOption = "//span[contains(text(),'Your saved credit and debit cards')]/../../following-sibling::div"
    _anotherPaymentOptions = "//span[contains(text(),' Another payment method')]/../../following-sibling::div"
    _creditCardRadioBTN = "//span[.='Credit card']/../../../../..//input[@id='pp-Cr-65']"
    _creditCardName = "//span[.='Credit card']/../..//label[.='Name on card']/following-sibling::input"
    _creditCardNo = "//span[.='Credit card']/../..//label[.='Card number']/following-sibling::input"
    _mon = "ppw-expirationDate_month"
    _year = "ppw-expirationDate_year"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    name = "nithish dev m"
    cardNo = "5337 4401 0009 4995"
    cvv = "168"

    def countNoOfDeliveryOption(self):
        count=len(self.driver.find_elements_by_xpath(self._anotherPaymentOptions))
        print(count)

    def paymentDetails(self):
        self.driver.implicitly_wait(2)
        self.elementClick(self._creditCardRadioBTN,"xpath")
        self.driver.implicitly_wait(2)
        self.sendKeys(self.name,self._creditCardName,"xpath")
        self.driver.implicitly_wait(2)
        self.sendKeys(self.cardNo,self._creditCardNo,"xpath")
        self.driver.implicitly_wait(2)
        mon = self.getElement(self._mon,"name")
        select = Select(mon)
        select.select_by_value('6')
        return True



