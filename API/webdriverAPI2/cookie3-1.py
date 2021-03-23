# 获取cookies，通过json.dump方法编码保存为json格式
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# # 保存cookies的文件
# file = 'cookies.json'
#
# # 点击登录
# driver.find_element_by_css_selector("#u1>:nth-child(2)").click()
#
# # 点击用户名登录
# WebDriverWait(driver,3).until(ec.element_to_be_clickable((By.ID,"TANGRAM__PSP_11__footerULoginBtn")))
# driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
#
# # 输入账号密码登录
# driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('15197230072')
# driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('ymfz520..')
# driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
# time.sleep(10)# 暂停10秒手动执行验证登录操作
#
# # 获取cookies并保存为json格式
# cookies = driver.get_cookies()
# fp = open(file,'w')
# json.dump(cookies,fp)
# fp.close()
# print("cookies文件保存成功!")
# driver.quit()

driver = webdriver.Chrome()
file = 'cookies.json'


# 获取网页的cookies
def get_cookies(test_url):
    driver.get(test_url)
    driver.maximize_window()
    # 点击登录
    driver.find_element_by_css_selector("#u1>:nth-child(2)").click()

    # 点击用户名登录
    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.ID, "TANGRAM__PSP_11__footerULoginBtn")))
    driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

    # 输入账号密码登录
    driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys('15197230072')
    driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('ymfz520..')
    driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
    time.sleep(30)  # 暂停10秒手动执行验证登录操作
    # 获取cookies并保存为json格式
    cookies = driver.get_cookies()
    with open(file, 'w') as fp:
        json.dump(cookies, fp)
    print("cookies文件保存成功!")
    driver.quit()


if __name__ == '__main__':
    get_cookies("https://www.baidu.com/")
