"""
Go to facebook, find the height and width of the username and password textfields,
 	compare the size to check the height and width same or not
"""

from selenium import webdriver

class Test_VerifyHieghtWidth:
    def test_verifyHieghtWidth(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        un = driver.find_element_by_id("email")
        pw = driver.find_element_by_id("pass")
        un_height = un.size.get('height')
        un_width = un.size.get('width')
        pw_height = pw.size.get('height')
        pw_width = pw.size.get('width')
        assert un_height == pw_height, "The height of the textboxes are not same"
        assert un_width == pw_width, "The width of the textboxes are not same"


