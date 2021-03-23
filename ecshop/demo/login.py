from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/ecshop/admin/privilege.php?act=login")

driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
#driver.find_element(By.CSS_SELECTOR,"[value='进入管理中心']").click()
driver.find_element(By.XPATH,"//input[@value='进入管理中心']").click()
#进入框架
driver.switch_to.frame("menu-frame")
driver.find_element(By.LINK_TEXT,"商品列表").click()

#出框架
driver.switch_to.default_content()

#进入框架
driver.switch_to.frame("main-frame")
#选择联想，，下拉框
sel=Select(driver.find_element(By.NAME,"brand_id"))
#sel=Select(driver.find_element_by_name("brand_id"))
#sel.select_by_index("3") #通过下标
#sel.select_by_value("9") #通过值
sel.select_by_visible_text("联想")

#点击搜索
driver.find_element(By.CSS_SELECTOR,"input[value=' 搜索 ']").click()
