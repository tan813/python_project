import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 开始时间
s_time = time.time()

driver.get("http://www.baidu.com")
driver.maximize_window()
e_time1 = time.time()

# 等待页面title = ‘百度一下，你就知道’
# WebDriverWait(driver,5).until(ec.title_is('百度一下，你就知道'))

# 等待页面title包含'你就知道'
# WebDriverWait(driver,5).until(ec.title_contains('你就知道'))

# 等待页面元素出现
# WebDriverWait(driver,5).until(ec.presence_of_element_located((By.ID,'kw')))

# 等待页面元素可见
# WebDriverWait(driver,5).until(ec.visibility_of_element_located((By.ID,'kw')))
# WebDriverWait(driver,5).until(ec.visibility_of(driver.find_element_by_id('kw')))

# 等待页面元素隐藏
# WebDriverWait(driver,5).until(ec.invisibility_of_element_located((By.ID,'kw')))

# 等待页面元素包含text文本
# WebDriverWait(driver,5).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR,'#s-top-left>:nth-child(1)'),'新闻'))

# 等待元素的值为selenium，一般用于输入框
# driver.find_element_by_id("kw").send_keys('selenium')
# WebDriverWait(driver,5).until(ec.text_to_be_present_in_element_value((By.ID,'kw'),'selenium'))

# 等待元素可点击
# WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.ID,'su')))

# 点击百度首页设置
driver.find_element_by_id('s-usersetting-top').click()
# WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.LINK_TEXT,'搜索设置')))
driver.find_element_by_link_text("搜索设置").click()


WebDriverWait(driver,5).until(ec.presence_of_element_located((By.ID,'s1_2')))
element1 = driver.find_element_by_id("s1_2")
element1.click()

# 等待元素被选中(两种)
# WebDriverWait(driver,5).until(ec.element_to_be_selected((element1)))
WebDriverWait(driver,5).until(ec.element_located_to_be_selected((By.ID,'s1_2')))

e_time2 = time.time()

print(e_time1-s_time,e_time2-s_time)


