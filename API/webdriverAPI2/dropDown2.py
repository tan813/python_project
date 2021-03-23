# select标签下拉框元素的选择

import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
file = 'file:///'+os.path.abspath('dropDown2.html')
driver.get(file)
driver.maximize_window()

# 通过索引选择
Select(driver.find_element_by_name('cars')).select_by_index(1)
sleep(1)
#
sleep(1)
# 通过value
Select(driver.find_element_by_name('cars')).select_by_value('aodi')
sleep(1)
# 通过选项文字
Select(driver.find_element_by_name('cars')).select_by_visible_text('宝马')
sleep(1)

# Select(driver.find_element_by_name('cars')).deselect_all()
driver.quit()