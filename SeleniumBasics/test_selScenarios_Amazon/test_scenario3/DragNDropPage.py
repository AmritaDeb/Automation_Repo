import time

class DragNDropPage:
    _sourceId="draggable"
    _targetId="droppable"
    _resultMsg="//div[@id='droppable']/p"
    global driver

    def __init__(self,driver):
        self.driver=driver

    def dragNdrop(self,action):
        source = self.driver.find_element_by_id(self._sourceId)
        target = self.driver.find_element_by_id(self._targetId)
        action.drag_and_drop(self,source,target).perform()
        time.sleep(5)
        msg = driver.find_element_by_xpath(self._resultMsg).text
        assert 'Dropped' in msg, "The text is not changed"