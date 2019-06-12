import time
class Inbox_Page:
    _composeBTN="//div[@role='button' and .='Compose']"
    _to="to"
    _sub="subjectbox"
    _msgBody="//div[@aria-label='Message Body']"
    _sendBTN="//div[@role='button' and .='Send']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCompose(self):
        self.driver.find_element_by_xpath(self._composeBTN).click()
        time.sleep(5)

    def sendEmail(self,email,sub,body):
        try:
            btn=self.driver.find_element_by_xpath(self._sendBTN)
            print("New mail window is opened")
            self.driver.find_element_by_name(self._to).send_keys(email)
            self.driver.find_element_by_name(self._sub).send_keys(sub)
            self.driver.find_element_by_xpath(self._msgBody).send_keys(body)
            btn.click()
            time.sleep(5)
        except Exception:
            print("New mail window is not opened")










