from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
element = driver.find_element_by_id("kw")
element.send_keys("selenium")
element.send_keys(Keys.CONTROL,'a')
element.send_keys(Keys.CONTROL,'c')

