import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://localhost/ecshop/admin/privilege.php?act=login")

driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element_by_link_text()
#driver.find_element(By.CSS_SELECTOR,"[value='进入管理中心']").click()
driver.find_element(By.XPATH,"//input[@value='进入管理中心']").click()




#进入框架
driver.switch_to.frame("menu-frame")
driver.find_element(By.LINK_TEXT,"商品列表").click()
#assert  driver.find_element(By.CSS_SELECTOR,"[href='goods.php?act=add']").text=="添加新商品"
#出框架
driver.switch_to.default_content()
#进入框架
driver.switch_to.frame("main-frame")
driver.find_element(By.LINK_TEXT,"添加新商品").click()
driver.find_element(By.NAME,"goods_name").send_keys("新北京布鞋")
sel=Select(driver.find_element_by_name("cat_id"))
sel.select_by_value("14")
driver.find_element(By.NAME,"shop_price").send_keys("4100")
#文件上传
driver.find_element(By.NAME,"goods_img_url").clear()
driver.find_element(By.NAME,"goods_img_url").send_keys("E:\\111.jpg")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"[value=' 确定 ']").click()
