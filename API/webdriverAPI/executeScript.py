# 设置浏览器窗口滚动条水平位置和垂直位置

from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(800,600)
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

sleep(2)

# 通过Javascript设置浏览器窗口滚动条位置
js = "window.scrollTo(0,450);"

driver.execute_script(js)
sleep(3)

driver.quit()