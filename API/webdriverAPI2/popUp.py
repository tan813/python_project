# 三种类型弹窗
# 1.警告类弹alert()，显示警告或其他信息，用于通知用户，下方只有一个【确认】按钮。
# 2.确认类弹窗confirm()，询问是否继续某种操作等功能，下方有【确认】和【取消】两种按钮。
# 3.消息类弹窗prompt()，需要输入一些信息，比如用户密码等，下方会有【确认】和【取消】按钮。

from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.implicitly_wait(10)
file = 'file:///' + os.path.abspath('pop_ups.html')
driver.get(file)

# alert弹窗
driver.find_element_by_css_selector('body>:nth-child(2)').click()
sleep(1)
# 切换到alert
alert = driver.switch_to.alert
# 打印alert文本
print('alert text:'+alert.text)
# 点击alert确认按钮
alert.accept()
# 打印操作
print('what you have done is : ' + driver.find_element_by_id('action').get_attribute('value'))
sleep(2)

# confirm弹窗
driver.find_element_by_css_selector('body>:nth-child(4)').click()
# 切换到alert
confirm = driver.switch_to.alert
# 打印confirm的文本
print('confirm text : ' + confirm.text)
sleep(2)
#点击confirm的取消按钮
confirm.dismiss()
print('what you have done is : ' + driver.find_element_by_id('action').get_attribute('value'))
sleep(2)

# prompt弹窗
driver.find_element_by_css_selector('body>:nth-child(6)').click()
# 切换到alert
prompt = driver.switch_to.alert
# prompt = Alert(driver)
# 打印prompt的文本
print('promopt text : ' + confirm.text)
# 输入信息
prompt.send_keys("test prompt")
sleep(1)
prompt.accept()
# 打印操作
print('what you have done is : ' + driver.find_element_by_id('action').get_attribute('value')) #打印刚才的操作
sleep(2)
driver.quit()