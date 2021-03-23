import time

from selenium import webdriver

driver=webdriver.Chrome()

driver.get("http://sz.ganji.com/")
driver.maximize_window()
driver.find_element_by_link_text("包吃包住").click()

handles = driver.window_handles
driver.switch_to.window(handles[-1])

print("当前页面title是:",driver.title)
time.sleep(5)
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
driver.find_element_by_css_selector("[id = 'write_resume_id']>:nth-child(2)>span").click()
# driver.find_element_by_xpath("//*[@id='write_resume_id']/div[2]/span").click()
# driver.find_element_by_css_selector("i.icon-wangfan").click()

time.sleep(2)

