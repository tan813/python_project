# ActionChains 类提供了鼠标操作的常用方法：
# perform()	执行所有ActionChains中存储的行为
# context_click()	右击

# 使用win32api/win32con库中keybd_event方法配合各键位键码,操作右键菜单

from time import sleep

import win32api
import win32clipboard
import win32con
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 设置复制内容text
text = "tanjinbai@jimilab.com"
# 打开粘贴板
win32clipboard.OpenClipboard()
# 清空粘贴板
win32clipboard.EmptyClipboard()
# 设置粘贴板内容
win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
# 关闭粘贴板线程
win32clipboard.CloseClipboard()
# 打开粘贴板
win32clipboard.OpenClipboard()
# 获取粘贴板内容
clipboard_content = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
# 关闭粘贴板线程
win32clipboard.CloseClipboard()

# 打开网易企业邮箱
# tanjinbai@jimilab.com
driver.get("https://qiye.163.com/login/")
driver.maximize_window()

# 点击账号密码登录
driver.find_element_by_id("switchNormalCtrl").click()

# 鼠标右击账号输入框
element = driver.find_element_by_id("accname")
ActionChains(driver).context_click(element).perform()

# selenium操作右击菜单
# 一、使用win32api/win32con包中keybd_event方法
# ①从右击菜单依次向下选择至“粘贴”
for i in range(1, 7):  # 循环6次方便看效果
    # 按下"↓"键并释放
    win32api.keybd_event(40, 0, 0, 0)
    win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
    sleep(1)
# 按下"Enter"回车键并释放
win32api.keybd_event(13, 0, 0, 0)
win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
sleep(2)

# ②清除输入框内容后直接ctrl+v粘贴
element.clear()
sleep(2)  # 停顿2s看效果
element.click()
sleep(2) # 停顿2s看效果
# 按下"crtl+v"
win32api.keybd_event(17, 0, 0, 0)
win32api.keybd_event(86, 0, 0, 0)
# 释放"crtl+v"
win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)

# 关闭浏览器
sleep(3)
driver.quit()
