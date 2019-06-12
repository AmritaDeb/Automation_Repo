from framework.base.Selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    _username = "ap_email"
    _continue = "continue"
    _password = "ap_password"
    _submit_button = "signInSubmit"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Method for login into Amazon.in using username & password, present in json file"""
    def loginAmazon(self,username,password):
        self.sendKeys(username,self._username)
        self.elementClick(self._continue,"id")
        self.driver.implicitly_wait(10)
        self.sendKeys(password,self._password)
        self.elementClick(self._submit_button,"id")
        self.driver.implicitly_wait(10)
        return True


