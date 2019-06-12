import time
class LoginPage:

    __username = "identifierId"
    __password = "password"
    __submitBTN = "//span[.='Next']"
    __inboxCount = "//a[.='Inbox']/../following-sibling::div"

    def __init__(self,driver):
        self.driver = driver

    def clickLogin(self,un,pw):
        self.driver.find_element_by_id(self.__username).send_keys(un)
        self.driver.find_element_by_xpath(self.__submitBTN).click()
        time.sleep(10)
        self.driver.find_element_by_name(self.__password).send_keys(pw)
        self.driver.find_element_by_xpath(self.__submitBTN).click()
        time.sleep(10)
    def fetchInboxCount(self):
        return self.driver.find_element_by_xpath(self.__inboxCount).text