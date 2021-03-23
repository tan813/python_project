# # 以下通过TouchActions类的scroll_from_element()
# # 方法无法实现滑动选择
# #
# from selenium import webdriver
# from time import sleep
#
# from selenium.webdriver import TouchActions
#
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option('w3c', False)
# driver = webdriver.Chrome(options=opt)
# driver.maximize_window()
# driver.get("http://www.jq22.com/yanshi4976")
# sleep(2)
#
# driver.switch_to.frame("iframe")
# driver.find_element_by_id("appDateTime").click()
#
# # 定位要滑动的年、月、日
# dwwos = driver.find_elements_by_class_name("dwwo")
# year = dwwos[0]
# month = dwwos[1]
# day = dwwos[2]
# action = TouchActions(driver)
# action.scroll_from_element(day,0,100).perform()
# sleep(3)
# driver.quit()

# 换一种ActionChains去滑动选择日期，具体情况目前只能根据每一个ul的高度去滑，
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.jq22.com/yanshi4976")
sleep(5)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()
dwwos = driver.find_elements_by_class_name("dwwo")
dwuls = driver.find_elements_by_class_name("dw-ul")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

action = ActionChains(driver)
action.click_and_hold(year)
action.move_by_offset(0, 108)
action.release().perform()
sleep(2)
