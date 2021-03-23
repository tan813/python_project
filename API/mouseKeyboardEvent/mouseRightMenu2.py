# 使用pyautogui库中typewrite或press方法，操作右键菜单

from time import sleep
import pyautogui


from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# 打开网页邮箱
driver.get("https://qiye.163.com/login/")
driver.maximize_window()

# 点击账号密码登录
driver.find_element_by_id("switchNormalCtrl").click()

# 鼠标右击账号输入框
element = driver.find_element_by_id("accname")

ActionChains(driver).context_click(element).perform()

# pyautogui.press模拟键盘依次按下多个按键，intervar是指列表中整个一轮操作的间隔时间不是指列表中每个按键的间隔时间
# pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down','enter'],presses=1,interval=1.0)

# 改成以下写法，能明显看出间隔时间
pyautogui.press(['down'],presses=6,interval=1.0)
pyautogui.press(['enter'])


# element.click()
# pyautogui.typewrite('down',interval=0.25)




sleep(2)
driver.quit()
