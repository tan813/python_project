import os

from selenium import webdriver

driver = webdriver.Chrome()
file = 'file:///'+os.path.abspath('upLoad.html')
print(file)
driver.get(file)
driver.maximize_window()
# driver.find_element_by_id('pic').send_keys(r'D:/projects/python_project/webdriverAPI2/upLoad.html')
driver.find_element_by_id('pic').send_keys(r'D:\projects\python_project\webdriverAPI2\test3.html')