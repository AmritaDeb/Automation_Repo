from framework.base.Selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _username = "username"
    _password = "password"
    _submit_button= "//input[@value='Log in']"
    _pypi_link="//a[@title='Python Package Index']"
    _Login_button="//a[contains(text(),'Log in')]"
    _installing_package= "//a[contains(text(),'Installing packages')]"
    _account_settings= "//*[contains(text(), 'Account settings')]"
    _uploading_package="//a[contains(text(),'Uploading packages')]"
    _login_page_element="//span[contains(text(),'Welcome back,')]"

    # def getusername(self):
    #     return self.driver.find_element(By.ID, self._username)
    #
    # def getpassword(self):
    #     return self.driver.find_element(By.ID, self._password)
    #
    # def getsubmitbutton(self):
    #     return self.driver.find_element(By.XPATH, self._submit_button)
    #
    #
    # def enterusername(self, username):
    #      self.getusername().send_keys(username)
    #
    # def enterpassword(self, password):
    #     self.getpassword().send_keys(password)
    #
    # def clicksubmitbutton(self):
    #     self.getsubmitbutton().click()

    def LoginPYPI(self, username, password):
        # Using Base Class Selenium Driver
        self.sendKeys(username, self._username)
        self.sendKeys(password, self._password)
        self.elementClick(self._submit_button, "xpath")
        return True

    def goToLoginPage(self):

        # self.driver.find_element(By.XPATH,self._pypi_link ).click()
        # self.driver.implicitly_wait(5)
        # self.driver.find_element(By.XPATH, self._Login_button).click()
        # self.driver.implicitly_wait(5)
        # Using Selenium Driver
        self.elementClick(self._pypi_link, "xpath")
        self.driver.implicitly_wait(5)
        self.elementClick(self._Login_button, "xpath")
        self.driver.implicitly_wait(5)
        return True

    def verify_login_successful(self):
        return self.elementPresenceCheck(self._login_page_element, "xpath")

    def gotoAccountSetting(self):
        self.elementClick(self._account_settings, "xpath")

    def goToInstallingpackage(self):
        self.elementClick(self._installing_package, "xpath")
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        return True

    def goToUploadPackage(self):
        self.elementClick(self._uploading_package, "xpath")
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        return True
