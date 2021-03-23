# 先打开所有窗口，再依次在每个窗口操作
# 3个句柄切换（以百度、搜狗、有道为例）

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window() # 窗口最大化

driver.get('https://www.baidu.com') # 在当前浏览器中访问百度
time.sleep(2)
print("百度窗口句柄是",driver.current_window_handle)# 输出当前窗口句柄（百度）
frist_handle = driver.current_window_handle

# 新开一个窗口，通过执行js来新开一个窗口,访问搜狗
js='window.open("https://www.sogou.com");'
driver.execute_script(js)
time.sleep(1)

# 再新开一个窗口，通过执行js来新开一个窗口，访问有道
js='window.open("http://www.youdao.com/");'
driver.execute_script(js)


handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
print("3个窗口时，句柄集合为",handles) # 输出句柄集合

i= 1
for handle in handles:# 切换窗口（切换到有道）
    print("第"+str(i)+"次循环句柄为"+handle)
    i = i +1
    if handle != frist_handle:
        driver.switch_to.window(handle)
        print("有道句柄"+driver.current_window_handle)  # 输出当前窗口句柄（有道）
        driver.find_element_by_id("translateContent").send_keys("selenium")  #有道翻译selenium
        driver.find_element_by_css_selector("button").click()
        #driver.find_element_by_css_selector("[data-rlog='search-popup-close-win']").click()
        driver.find_element_by_css_selector("[class='close js_close']").click()  #关闭弹窗
        #driver.get_screenshot_as_file("D:\windows\\youdao.png")  # 截图  可自定义截图后的保存位置(D:\windows)和图片命名(youdao.jpg)
        time.sleep(5)
        break
driver.close() #关闭当前窗口（有道）

#handles = driver.window_handles # 获取当前窗口句柄集合（列表类型）
print("有道窗口关闭后，句柄集合为",handles) # 输出句柄集合

for handle in handles:# 切换窗口（切换到搜狗）
    if handle != frist_handle:
        driver.switch_to.window(handles[-1]) #此时只剩两个句柄，取最后一个
        #print(driver.current_window_handle)  # 输出当前窗口句柄（搜狗）
        driver.find_element_by_id("query").send_keys("selenium")  #搜狗搜索selenium
        driver.find_element_by_id("stb").click()
        time.sleep(2)  #等待2s为了截完整搜索结果图
        #driver.get_screenshot_as_file("D:\windows\\sougou.png")  # 截图  可自定义截图后的保存位置和图片命名
        time.sleep(5)
        break
driver.close() #关闭当前窗口（搜狗）d

#driver.switch_to_window(frist_handle) #切换回百度窗口
driver.switch_to.window(handles[0]) #切换回百度窗口
driver.find_element_by_id("kw").send_keys("selenium")  #百度搜索selenium
driver.find_element_by_id("su").click()
time.sleep(2) #等待2s为了截完整搜索结果图
#driver.get_screenshot_as_file("D:\windows\\baidu.png")  #截图  可自定义截图后的保存位置和图片命名
time.sleep(5)
driver.quit() #退出浏览器