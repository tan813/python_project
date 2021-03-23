from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qzone.qq.com/")
# driver.maximize_window()

# 切入登录框架
driver.switch_to.frame("login_frame")

# 点击账号密码登录
driver.find_element_by_id("switcher_plogin").click()

# 输入账号密码点登录
driver.find_element_by_id("u").send_keys("240841985")
driver.find_element_by_id("p").send_keys("ymfz520+-")
sleep(1)
driver.find_element_by_id("login_button").click()
sleep(1)
# 移动验证码滑块
distance = 163
# 切入验证框架
driver.switch_to.frame("tcaptcha_iframe")
WebDriverWait(driver,5).until(ec.presence_of_element_located((By.ID,"slideBlock")))
element = driver.find_element_by_id("slideBlock")

# ActionChains(driver).click_and_hold(element).move_by_offset(distance,0).release().perform()
action = ActionChains(driver)
action.click_and_hold(element)
action.move_by_offset(distance,0)
action.release().perform()

sleep(3)
# driver.quit()
