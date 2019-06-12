"""
1. Open any browser of your choice, say Mozilla Firefox
2. Navigate to https://www.gmail.com
3. Enter a valid Email Id or Phone Number
4. Click Next button
5. Enter Password and click “Sign in” button.
6. Verify that gmail is logged in successfully.
7. Click compose button and verify that a new mail window is opened.
8. Enter a Email Id
9. Enter some subject, say “Test Mail”
10. Enter some text in body
11. click send button.
"""

from selenium import webdriver
import time
import re
from test_selScenarios.test_scenario2.Login_Page import Login_Page
from test_selScenarios.test_scenario2.Inbox_Page import Inbox_Page

class Test_Gmail:
    def test_gmail(self):
        un = "amritadebbarman@gmail.com"
        pw = "161amrita2541"
        item=50
        driver=webdriver.Chrome(executable_path="D:\\TestYantra\\python\\TY\\chromedriver.exe")
        driver.get("https://www.gmail.com")
        driver.maximize_window()
        driver.implicitly_wait(10)
        Login_Page(driver).gmailLogin(un,pw)
        assert 'Inbox' in driver.title, "Gmail is not logged in"
        inbox=Inbox_Page(driver)
        inbox.clickOnCompose()
        inbox.sendEmail("amritadebbarman@gmail.com","Test Mail", "Good Evening")

ob=Test_Gmail()
ob.test_gmail()