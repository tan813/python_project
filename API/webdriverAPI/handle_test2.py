# 京东两个窗口句柄的切换

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.jd.com")
time.sleep(1)

# 获取当前页面句柄
handle1 = driver.current_window_handle
print(handle1)

# 点击秒杀
driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[4]/ul[1]/li[1]/a").click()
time.sleep(1)
# 获取当前页面句柄
print(driver.current_window_handle)

# 获取所有页面句柄
all_handles = driver.window_handles
print(all_handles)

# 将第一个窗口的句柄与所有句柄进行比较
for handle in all_handles:
    # 如果该句柄与第一个窗口的句柄不一样，切换到该句柄，才能定位另一个窗口内的元素
    if handle != handle1:
        driver.switch_to.window(handle)

# 大牌闪购在第二个窗口
driver.find_element_by_link_text("大牌闪购").click()
time.sleep(2)

# 将第一个窗口的句柄与所有句柄进行比较
for handle in all_handles:
    # 如果该句柄与第一个窗口的句柄一样，切换到该句柄，才能定位第一个窗口内的元素
    if handle == handle1:
      driver.switch_to.window(handle)

# 拍卖在第一个窗口
driver.find_element_by_link_text("拍卖").click()
time.sleep(1)

