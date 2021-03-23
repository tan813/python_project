# pyautogui模拟键盘点击操作右键菜单保存图片

from time import sleep
import pyautogui


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").click()

WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.ID,'s_lg_img')))
element = driver.find_element_by_id('s_lg_img')
ActionChains(driver).context_click(element).perform()

# 找到图片另存为菜单
pyautogui.typewrite(['down','down','down','down','down','down','down','enter','enter'],interval=1.5)
sleep(2)
driver.quit()

