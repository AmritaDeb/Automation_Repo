import time
class Login_Page:
    _username="identifierId"
    _password="password"
    _nextBTN="//span[.='Next']"

    def __init__(self,driver):
        self.driver=driver

    def gmailLogin(self,un,pw):
        self.driver.find_element_by_id(self._username).send_keys(un)
        self.driver.find_element_by_xpath(self._nextBTN).click()
        time.sleep(5)
        self.driver.find_element_by_name(self._password).send_keys(pw)
        self.driver.find_element_by_xpath(self._nextBTN).click()
        time.sleep(5)


