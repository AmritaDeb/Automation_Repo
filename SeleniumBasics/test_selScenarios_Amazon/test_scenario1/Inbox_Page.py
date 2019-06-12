import re
import time
class Inbox_Page:
    _primaryTrue="//div[@aria-selected='true' and .='Primary']"
    _primaryBTN="//div[@class='aKz' and .='Primary']"
    _totalCount="//div[@class='aeH']/div/div[1]/div[2]/div[1]/span/div[1]/span/span[2]"
    _pageRange="//div[@class='aeH']/div/div[1]/div[2]/div[1]/span/div[1]/span/span[1]/span[2]"
    _inboxItem="//div[@class='UI']/div/div[1]/div[2]//tr"
    # _senderName="(//div[@class='UI']/div/div[1]/div[2]//tr)["+ i +"]/td[5]/div[2]/span/span"
    # _sub="(//div[@class='UI']/div/div[1]/div[2]//tr)["+ i +"]/td[6]/div/div/div/span/span"
    _progress="//div[@class='aeH']/div[2]/div[1]/div[2]/div[1]/span[@class='Di']/div[@aria-label='Older']"

    def __init__(self,driver):
        self.driver=driver

    def isPrimarySelected(self):
        try:
            self.driver.find_element_by_xpath(self._primaryTrue)
            print("Primary section is selected")
        except Exception:
            self.driver.find_element_by_xpath(self._primaryBTN).click()

    def countEmails(self):
        total=self.driver.find_element_by_xpath(self._totalCount)
        count = int(re.sub(r"[^\d.]", "", total.text))
        return count

    def fetchNameSub(self,i,count):
        pageRange1 = int(self.driver.find_element_by_xpath(self._pageRange).text)
        print(pageRange1)
        j=i//pageRange1
        print(j)
        if i<=pageRange1:
            name = self.driver.find_element_by_xpath("(//div[@class='UI']/div/div[1]/div[2]//tr)[" + str(i) + "]/td[5]/div[2]/span/span").text
            sub = self.driver.find_element_by_xpath("(//div[@class='UI']/div/div[1]/div[2]//tr)[" + str(i) + "]/td[6]/div/div/div/span/span").text
            print("The Sender Name is: ", name)
            print("The Subject is: ", sub)
        else:
            for x in range(0,j):
                self.driver.find_element_by_xpath("//div[@role='button' and @aria-label='Older']").click()
                time.sleep(3)
                pageRange2 = int(self.driver.find_element_by_xpath(self._pageRange).text)
                if pageRange2//pageRange1==j:
                    name = self.driver.find_element_by_xpath("(//div[@class='UI']/div/div[1]/div[2]//tr)[" + str(pageRange1) + "]/td[5]/div[2]/span/span").text
                    sub = self.driver.find_element_by_xpath("(//div[@class='UI']/div/div[1]/div[2]//tr)[" + str(pageRange1) + "]/td[6]/div/div/div/span/span").text
                    print("The Sender Name is: ", name)
                    print("The Subject is: ", sub)
                    break
                elif pageRange2//pageRange1==j+1:
                    name = self.driver.find_element_by_xpath("(//div[@class='UI']/div/div[1]/div[2]//tr)[" + str(pageRange2 - i) + "]/td[5]/div[2]/span/span").text
                    sub = self.driver.find_element_by_xpath("(//div[@class='UI']/div/div[1]/div[2]//tr)[" + str(pageRange2 - i) + "]/td[6]/div/div/div/span/span").text
                    print("The Sender Name is: ", name)
                    print("The Subject is: ", sub)
                    break





