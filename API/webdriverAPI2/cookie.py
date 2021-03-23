# 通过浏览器调试获取登录后的cookies，然后利用获取到的cookies自动登录

from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()
cookies = [
    {'domain': '.baidu.com', 'expiry': 1611746501, 'httpOnly': False, 'name': 'BA_HECTOR', 'path': '/', 'secure': False,
     'value': '0o2l2h80808h2k406m1g12fll0q'},
    {'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False,
     'value': '33425_33518_33242_33258_33273_31254_33284_33335_26350_22158'},
    {'domain': '.baidu.com', 'expiry': 1643278900, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False,
     'value': '5FB50CB3E36C0125D3F8D631562FFFE4:FG=1'},
    {'domain': '.baidu.com', 'expiry': 3759226547, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False,
     'value': '5FB50CB3E36C01251D45DF156B0841FC'},
    {'domain': '.baidu.com', 'expiry': 3759226547, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False,
     'value': '1611743014'},
    {'domain': 'www.baidu.com', 'expiry': 1612606901, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False,
     'value': '12314453'},
    {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '1'}
           ]
sleep(3)
for cookie in cookies:

    driver.add_cookie(cookie)

driver.refresh()
