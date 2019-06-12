"""
Scenario 1:
1. Open a browser of your choice say Mozilla Firefox using Gecko Driver
2. Navigate to Gmail (https://www.gmail.com)
3. Login to your Gmail with correct credentials.
4. Verify that by default “Primary” section is selected.
5. If not click on the Primary tab.
6. Get the count of the total number of emails in the Primary tab.
7. Get the name of the sender and subject of Nth Email of your inbox.
8. Write a method to get the name of the sender and subject of email of your inbox.
"""

from selenium import webdriver
import time
import re
from SeleniumBasics.test_selScenarios_Amazon.test_scenario1.Login_Page import Login_Page
from SeleniumBasics.test_selScenarios_Amazon.test_scenario1.Inbox_Page import Inbox_Page


class Test_Gmail:
    def test_gmail(self):
        un = "amritadebbarman@gmail.com"
        pw = "161amrita2541"
        item=100
        driver=webdriver.Chrome(executable_path="D:\\TestYantra\\python\\TY\\chromedriver.exe")
        driver.get("https://www.gmail.com")
        driver.maximize_window()
        driver.implicitly_wait(10)
        Login_Page(driver).gmailLogin(un,pw)
        inbox=Inbox_Page(driver)
        inbox.isPrimarySelected()
        count=inbox.countEmails()
        print(count)
        inbox.fetchNameSub(item,count)

ob=Test_Gmail()
ob.test_gmail()