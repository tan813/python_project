# TouchActions 长按并滑动滑块
# 无法实现
import os

from selenium import webdriver
from selenium.webdriver import TouchActions

mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(5)
file = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(file)

e1 = driver.find_element_by_id('submitBTN')

action = TouchActions(driver)
action.scroll_from_element(e1,0,2000).perform()

driver.switch_to.frame('iframeResult')
e2 = driver.find_element_by_id('draggable')
e2_x = e2.location.get('x')
e2_y = e2.location.get('y')


e3 = driver.find_element_by_id('droppable')
e3_x = e3.location.get('x')
e3_y = e3.location.get('y')

action1 = TouchActions(driver)
action1.tap_and_hold(e2_x,e2_y)
action1.move(e2_x+50,e2_y).release(e2_x+50,e2_y)
action1.perform()
#
# # 执行
# action.perform()
