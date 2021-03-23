import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/ecshop/admin/privilege.php?act=login")

driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin12345")
#driver.find_element(By.CSS_SELECTOR,"[value='进入管理中心']").click()
driver.find_element(By.XPATH,"//input[@value='进入管理中心']").click()

#进入框架
driver.switch_to.frame("menu-frame")
driver.find_element(By.LINK_TEXT,"商品列表").click()
#出框架
driver.switch_to.default_content()
# 进入框架
driver.switch_to.frame("main-frame")

# 定位一组元素
# 通过右边回收站图标删除
# delArray=driver.find_elements(By.CSS_SELECTOR,"img[src='images/icon_trash.gif']")
# delArray[0].click()

# 弹出窗口
# alert=driver.switch_to.alert
# alert.accept()
# 批量删除
Array=driver.find_elements(By.NAME,"checkboxes[]")
# for a in range(3):
for a in (0,1,2):
 Array[a].click()
sel=Select(driver.find_element(By.ID,"selAction"))
sel.select_by_value("trash")
#定位到弹窗
alert=driver.switch_to.alert
alert.accept()