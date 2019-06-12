"""
	Go to plus2net.com, select the checkbox and check the textbox is enabled or not
"""

from selenium import webdriver

class Test_VerifyTextbox:
    def test_verifyTextbox(self):
        driver = webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.plus2net.com/javascript_tutorial/enable-disable-demo.php")
        chkbx = driver.find_element_by_name("others")
        chkbx.click()
        condition1 = chkbx.is_selected()
        txtbx = driver.find_element_by_name("other_text")
        condition2 = txtbx.is_enabled()
        assert condition1 and condition2 , "Textbox is disabled"
