import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(1)

# 通过id
# driver.find_element_by_css_selector("#kw").send_keys(1234)
# time.sleep(1)

# 通过标签
# driver.find_element_by_css_selector("input").send_keys()

# 通过其他属性
# driver.find_element_by_css_selector("[autocomplete= 'off']").send_keys("1234")
# time.sleep(1)

# 通过标签+其他属性组合
# driver.find_element_by_css_selector("input[autocomplete = 'off']").clear()
# time.sleep(1)
#
# 通过两个其他属性组合
# driver.find_element_by_css_selector("[autocomplete= 'off'][name = 'wd']").clear()
# time.sleep(1)
#
# driver.find_element_by_css_selector("input#kw").clear()

# 层级定位法定位输入框######################################################

# 通过子元素
# driver.find_element_by_css_selector("form#form>span>input").send_keys(123)
# form表单下第1个span标签，第8个标签
# driver.find_element_by_css_selector("form[name = 'f'][action = '/s']>span>input").clear()

# 通过后代元素
# driver.find_element_by_css_selector("form#form #kw").send_keys(123)

# 定位父元素的(倒数)第n个字子节点##########################################
# ①form表单下第2个span类型的标签，第9个标签 （这里的排序是所有标签一起排序，并且包含静态标签而不是按标签分类后的排序）
# driver.find_element_by_css_selector("form#form>:nth-child(9)>input").click()

# ②(不需要从form表单往下找，需要加上span标签类型)
# driver.find_element_by_css_selector("span:nth-child(9)>input").click()

# ③第2个span类型的标签标签（按标签分类后的排序）
# driver.find_element_by_css_selector("span:nth-of-type(2)>input").click()

# 定位输入框
# ④不从form表单往下找，作为子元素的倒数第3个input标签
# driver.find_element_by_css_selector("input:nth-last-child(3)").send_keys(123)

# 根据兄弟节点定位####################################################
# ①通过相邻兄弟节点定位，且span标签是input标签后的第一个标签
# driver.find_element_by_css_selector("input+span>input").send_keys(123)
# time.sleep(1)

# ②定位兄弟节点定位一组元素
# elements = driver.find_elements_by_css_selector("input~span")
# for element in elements:
#  print (element)

# class属性值中含有空格##################################################
# driver.find_element_by_class_name("bg s_btn").click()
# 两种修改方法
# driver.find_element_by_class_name("bg.s_btn").click()
# driver.find_element_by_css_selector("[class = 'bg s_btn']").click()
# time.sleep(1)




driver.quit()