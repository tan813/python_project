from selenium import webdriver        # 导入selenium框架包中的webdriver模块
driver = webdriver.Chrome()           # 调用webdriver模块中Chrome方法自动打开谷歌浏览器
driver.get("http://baidu.com")        # 打开你要测试的网址