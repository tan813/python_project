# 打开一个窗口进行操作会打开第二个窗口，在第二个窗口进行操做会打开第3个窗口
# 3个窗口句柄切换

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://sz.ganji.com/")
driver.maximize_window()
print("【深圳赶集网】句柄",driver.current_window_handle)
print("当前页面title",driver.title)
time.sleep(1)
print("----------------------------------")

# 点击包吃包住
driver.find_element_by_link_text("包吃包住").click()
time.sleep(5)

# 获取所有句柄
h = driver.window_handles
print("打开两个窗口时所有句柄:",h)

# 切换至【深圳找工作窗口】
driver.switch_to.window(h[1])
time.sleep(2)

# 验证是否切换成功
print("当前页面句柄"+driver.current_window_handle)
print("当前页面title",driver.title)
print("----------------------------------")

# 点击二手房
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[3]/a").click()
time.sleep(3)

# 此时打开三个窗口。需要重新获取句柄
h1 = driver.window_handles
print("打开三个窗口时所有句柄:",h1)

# 切换至深圳二手房页面
driver.switch_to.window(h1[2])

#验证是否切换成功
print("当前页面句柄"+driver.current_window_handle)
print("当前页面title",driver.title)
print("----------------------------------")
driver.find_element_by_link_text("土地").click()
