from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 强制等待,设置固定的休眠时间，执行sleep()后线程休眠
# sleep(5)

# 隐式等待，是设置的全局等待，对页面中所有元素设置加载时间，超出设置时间抛出异常
# driver.implicitly_wait(5)


driver.get('http://sz.ganji.com/')

driver.maximize_window()

driver.find_element_by_link_text("包吃包住").click()
sleep(6)

handle = driver.window_handles
driver.switch_to.window(handle[-1])
print("当前页面title：",driver.title)

js = "window.scrollTo(0,document.body.scrollHeight);"
driver.execute_script(js)
# sleep(5)

# 报错：element click intercepted
# 元素渠道合作被其他元素遮挡，点击不到

# ①by_xpath 叉掉遮挡页面
# driver.find_element_by_xpath("//*[@id='write_resume_id']/div[2]/span").click()

# ①by_css_selector 叉掉遮挡页面
driver.find_element_by_css_selector("#write_resume_id>:nth-child(2)>span").click()

# ②不用叉掉，直接找到并点击
# element = driver.find_element_by_link_text("渠道合作")
# driver.execute_script("arguments[0].click();",element)

# ③不用叉掉，直接找到并点击
# element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
# webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

# 显式等待，是针对某个特定的元素设置的等待时间
# WebDriverWait()默认0.5s刷新一次
WebDriverWait(driver,5,0.5).until(lambda driver:driver.find_element_by_link_text("渠道合作")).click()

sleep(3)
driver.quit()

