"""
Scenario 3:
1. Open a browser of your choice say Mozilla Firefox
2. Navigate to http://jqueryui.com/droppable/ webpage.
3. Consider “Drag me to my target” as a source and “Drop here” as a target.
4. Write a code to perform drag and drop operation from source to target.
5. After drag and drop verify the operation is successfully by checking the color property of CSS and
also verify text change. (Use assert statement to verify that color and text are as expected.)
"""

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
from test_selScenarios.test_scenario3.DragNDropPage import DragNDropPage

class Test_DragNDrop:
    def dragNdrop(self):
        driver=webdriver.Chrome(executable_path="D:\\TestYantra\\python\\TY\\chromedriver.exe")
        driver.get("http://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(5)
        frame=driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(frame)
        source=driver.find_element_by_id("draggable")
        target=driver.find_element_by_id("droppable")
        action=ActionChains(driver)
        action.drag_and_drop(source,target).perform()
        time.sleep(5)
        msg=driver.find_element_by_xpath("//div[@id='droppable']/p").text
        assert 'Dropped' in msg, "The text is not changed"
        print("The text is changed")
        bgcolor=target.value_of_css_property("background")
        rgb=bgcolor.split('n')
        hexbgcolor=Color.from_string(rgb[0]).hex
        assert '#fffa90' == hexbgcolor,'The color is not changed'
        print("The color is changed")

ob=Test_DragNDrop()
ob.dragNdrop()