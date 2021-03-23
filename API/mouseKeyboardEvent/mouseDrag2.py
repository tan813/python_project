import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)

driver.switch_to.frame('iframeResult')  # 切换iframe
loc1 = driver.find_element_by_css_selector('#draggable')
action = ActionChains(driver)
# 点击元素并按住
action.click_and_hold(loc1)

# ①移动到目标位置等待2s再释放
action.move_by_offset(250,0)
action.perform()
# 等待2s再释放
time.sleep(2)
action.reset_actions()
# action.release().perform()
# action.reset_actions()是清除已存储在本地和远程端的操作，行为链已经被清除了，
# 再调用release方法时报错，删掉action.release().perform()
# 或者:
# action = ActionChains(driver)
# action.release().perform()


# ②移动到目标位置后就释放
# action.move_by_offset(250,0)
# action.release().perform()

time.sleep(2)
driver.quit()
