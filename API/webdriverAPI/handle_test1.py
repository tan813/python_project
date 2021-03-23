# 1.selenium浏览器基本操作
# 2.发现需要且句柄的问题

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(1)

# 窗口最小化
driver.minimize_window()
time.sleep(1)

# 窗口最大化
driver.maximize_window()
time.sleep(1)

#刷新
driver.refresh()
time.sleep(1)

# 获取title
window_title = driver.title
print("当前页面的title是:"+window_title)

# 获取url
window_url = driver.current_url
print("当前页面的title是:"+window_url)

# 获取百度首页句柄
window_handle = driver.current_window_handle
print("当前页面的句柄是:"+window_handle)

# 点击新闻后，获取当前打开的所有窗口的句柄
driver.find_element_by_link_text("新闻").click()
all_handles = driver.window_handles
print("当前页面的句柄是:"+driver.current_window_handle)
print("当前所有窗口的句柄：",all_handles)

driver.switch_to.window(all_handles[1])

driver.find_element(By.LINK_TEXT,"国内").click()
time.sleep(1)

#后退
driver.back()
time.sleep(1)

#前进
driver.forward()

