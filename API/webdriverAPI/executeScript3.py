# selenium execute_script() 处理特殊文本框,以12306首页为例

# 1.检索框：可以直接输入文本，但必须要点击根据输入的文本检索出来的下拉列表的某一项（出发地、返回地）
# 2.日期框：无法直接输入文本，必须要选择某一天的日期并点击才会填入文本框（出发时间）
# 3.置灰的文本框：无法直接输入文本(executeScript2.py)
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.12306.cn/index/")

sleep(3)

# driver.find_elements_by_css_selector("li.active[1]>a")
driver.find_element_by_css_selector("i.icon-wangfan").click()

sleep(2)

go_date = driver.find_element_by_id("go_date")

from_date = driver.find_element_by_id("from_date")

a = driver.find_element_by_id("fromStationFan")

j = driver.find_element_by_id("fromStationFanText")

# start_area_js = '''
#                 var a = document.getElementById("fromStationFan");
#                 a.value = 'SHH';
#                 '''
# driver.execute_script(start_area_js)
#
# start_input_js = '''
#                 var j = document.getElementById('fromStationFanText');
#                 j.className = 'input inp-txt_select';
#                 j.value = '上海';
#                 '''
# driver.execute_script(start_input_js)


js = """
var arg1 = arguments[0]
var arg2 = arguments[1]
var arg3 = arguments[2]
var arg4 = arguments[3]
arg1.value = 'SHH'
arg2.value = '上海'
arg3.readonly = false;
arg3.value = '2020-09-16'
arg4.readonly = false;
arg4.value = '2020-10-02'

"""
driver.execute_script(js,a,j,go_date,from_date)

sleep(3)
driver.quit()
