# 在页面中的textarea文本框中输入内容（置灰文本框输入）
import os
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

# driver.get("D:\\projects\\python_project\\webdriverAPI\\textarea.html")
file = 'file:///'+os.path.abspath('textarea.html')
driver.get(file)
sleep(2)

# text定义输入的内容


js = """
    var text = "2020年9月15日"
    var a = document.getElementById('id')
    a.readonly = false;
    a.value=text;
"""

driver.execute_script(js)

sleep(2)

driver.quit()
