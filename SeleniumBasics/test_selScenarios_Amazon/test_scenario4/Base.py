from selenium import webdriver
import time

class Base:
    def launchBrowser(self,browser):
        if browser=='Chrome':
            driver=webdriver.Chrome(executable_path="D:\\TestYantra\\python\\TY\\chromedriver.exe")
        elif browser=='Firefox':
            driver=webdriver.Firefox(executable_path="D:\\TestYantra\\python\\TY\\geckodriver.exe")
        return driver
