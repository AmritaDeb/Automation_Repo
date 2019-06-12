from selenium import webdriver

driver=webdriver.Chrome(executable_path="D:\TestYantra\python\selenium\chromedriver.exe")
driver.get("https://google.com")
driver.close()