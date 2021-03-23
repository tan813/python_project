# 使用json.load方法解码，添加cookies实现免密登录
import json
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
# 保存cookies的文件
file = 'cookies.json'


# 打开需要登录的网站
def open_url(test_url):
    driver.get('http://'+test_url)
    driver.implicitly_wait(5)
    driver.maximize_window()


# 向浏览器添加保存的cookies
def add_cookies():
    with open(file, 'r') as fp:
        cookies = json.load(fp)
    for cookie in cookies:
        # ①直接删除cookie中的有效期属性'expiry'
        if 'expiry' in cookie:
            # del cookie['expiry']
            cookie.pop('expiry')

        # ②将'expiry'属性的值转成整数
        # if 'expiry' in cookie and 'expiry' is not None:
        #     cookie['expiry'] = int(cookie['expiry'])
        # driver.add_cookie(cookie)


if __name__ == '__main__':
    # 输入要打开的网站并打开
    url = input("输入要打开的网站:")
    open_url(url)
    sleep(3)
    # 添加cookies后刷新页面，实现免密登录
    add_cookies()
    driver.refresh()
    sleep(3)
    # 关闭浏览器
    driver.quit()
