# 网易企业邮箱登录界面，使用鼠标键盘操作复制元素内容
# 粘贴到登入输入框

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://qiye.163.com/login/")
driver.maximize_window()

# 定位网易企业邮箱首页"新用户开通按钮"
text = driver.find_element_by_link_text("新用户开通")

# 获取元素坐标
text_x = text.location.get('x')
text_y = text.location.get('y')
# 获取元素长宽
size_wid = text.size.get('width')
size_hei = text.size.get('height')

action = ActionChains(driver)
# 将鼠标移动到"新用户开通"元素前面一点，假定为x点
action.move_by_offset(text_x - 5, text_y)
# 按住鼠标左键并移动，选择"新用户开通元素"
action.click_and_hold()
# 此时移动，相对于x点的坐标而言而不是原点坐标
action.move_by_offset(size_wid + 5, 0)
action.release()
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)

action.perform()
# 点击账号密码登录
driver.find_element_by_id("switchNormalCtrl").click()
# 定位账号输入框
input = driver.find_element_by_id("accname")
# 键盘事件粘贴

action = ActionChains(driver)
action.key_down(Keys.CONTROL, input).send_keys('v').key_up(Keys.CONTROL).perform()

action.send_keys(Keys.TAB).perform()

# driver.quit()
