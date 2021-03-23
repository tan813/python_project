# 非select标签下拉框元素的定位

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


driver.get("http://www.baidu.com")
driver.maximize_window()

# 百度首页设置
driver.find_element_by_id('s-usersetting-top').click()
# WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.LINK_TEXT,'搜索设置')))
driver.find_element_by_link_text("高级搜索").click()
WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.ID,"adv-setting-gpc")))
# 时间
driver.find_element_by_css_selector("span#adv-setting-gpc>:nth-child(2)").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='adv-setting-gpc']/div/div[2]/div[2]/p[3]").click()
# 格式
driver.find_element_by_css_selector("span#adv-setting-ft>:nth-child(2)").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='adv-setting-ft']/div/div[2]/div[2]/p[4]").click()

# driver.get("https://work.weixin.qq.com/")
# driver.maximize_window()
# # 立即注册
# WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.CLASS_NAME,'index_head_info_pCDownloadBtn')))
# driver.find_element_by_class_name("index_head_info_pCDownloadBtn").click()
#
# 下拉框之后还有一层
# driver.find_element_by_id("corp_industry").click()
# driver.find_element_by_xpath('//*[@id="corp_industry"]/div/table/tbody/tr/td[1]/div[5]/a').click()
# driver.find_element_by_xpath('//*[@id="corp_industry"]/div/table/tbody/tr/td[2]/div[5]/div[3]/a').click()

driver.quit()
