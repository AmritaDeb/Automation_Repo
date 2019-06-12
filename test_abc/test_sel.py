
"""
driver.find_element(By.TAG_NAME)
driver.find_element_by_tag_name()

driver.find_element(By.ID)
driver.find_element_by_id()

driver.find_element(By.NAME)
driver.find_element_by_name()

driver.find_element(By.CLASS_NAME)
driver.find_element_by_class_name()

driver.find_element(By.LINK_TEXT)
driver.find_element_by_link_text()

driver.find_element(By.PARTIAL_LINK_TEXT)
driver.find_element_by_partial_link_text()

driver.find_element(By.CSS_SELECTOR)
driver.find_element_by_css_selector()

driver.find_element(By.XPATH)
driver.find_element_by_xpath()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(executable_path="D:\\TestYantra\\python\\selenium\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.gmail.com")
try:
       un = WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID,"identifierId"))
finally:
# driver.implicitly_wait(5)
# driver.find_element_by_id("identifierId").send_keys("amritadebbarman@gmail.com")
       un.send_keys("amritadebbarman@gmail.com")
# driver.find_element_by_xpath("//span[.='Next']").click()
# time.sleep(2)
# driver.find_element_by_name("password").send_keys("161amrita2541")
# driver.find_element_by_xpath("//span[.='Next']").click()

# elem = driver.find_element_by_xpath(".//*[@id='SORM_TB_ACTION0']")
# elem.click()
# try:
#        elem = driver.find_element_by_xpath(".//*[@id='SORM_TB_ACTION0']")
#        elem.click()
# except NoSuchElementException:
#        pass
#
# driver.close()