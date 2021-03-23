# webdriver操作cookie的方法:
# get_cookies() 获得所有cookie 信息
# get_cookie(name) 返回特定name 的cookie 信息
# add_cookie(cookie_dict) 添加cookie，必须有name 和value 值
# delete_cookie(name) 删除特定(部分)的cookie 信息
# delete_all_cookies() 删除所有cookie 信息
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

#  获得指定name的cookie信息
cookie1 = driver.get_cookie('H_PS_PSSID')
cookie2 = driver.get_cookie('BAIDUID')
print(cookie1)
print(cookie2)
print('========================================')

# 添加cookie信息
driver.add_cookie({'name':'aaaaaa','value':'bbbbbbbbbb'})

# 删除指定name的cookie信息
driver.delete_cookie('aaaaaa')

# 获得所有cookie信息，登录前的
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
print('=========================================')
# 只打印name、value信息
for cookie in cookies:
    print("%s -> %s"%(cookie['name'],cookie['value']))

time.sleep(2)
driver.quit()