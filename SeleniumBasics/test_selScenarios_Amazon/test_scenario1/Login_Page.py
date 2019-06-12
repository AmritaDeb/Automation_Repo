import time
class Login_Page:
    username="identifierId"
    password="password"
    nextBTN="//span[.='Next']"

    def __init__(self,driver):
        self.driver=driver

    def gmailLogin(self,un,pw):
        self.driver.find_element_by_id(self.username).send_keys(un)
        self.driver.find_element_by_xpath(self.nextBTN).click()
        time.sleep(5)
        self.driver.find_element_by_name(self.password).send_keys(pw)
        self.driver.find_element_by_xpath(self.nextBTN).click()
        time.sleep(5)


