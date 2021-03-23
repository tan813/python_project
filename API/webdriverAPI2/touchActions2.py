# python selenium TouchActions模拟移动端触摸操作
# 百度首页搜索selenium，通过scroll_from_element()方法滑动到最底部
import time
from selenium import webdriver
from selenium.webdriver import TouchActions


mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.baidu.com/")
# 定位输入框
el = driver.find_element_by_id('index-kw')
# 定位‘百度一下’按钮
el_search = driver.find_element_by_id('index-bn')
el.send_keys('selenium测试')
action = TouchActions(driver)
# 点击
action.tap(el_search).perform()
# 滑动到最底部
# 重新定位“百度一下”元素,并重新创建TouchActions对象
action = TouchActions(driver)
e2 = driver.find_element_by_id('se-bn')
action.scroll_from_element(e2,0,5000)
action.perform()
time.sleep(3)

# driver.quit()