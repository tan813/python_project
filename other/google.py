from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://translate.google.cn/")
driver.maximize_window()

list_test=['product description 1','product description 2']
item = []
for i in range(0,2):
    try:
        body_text = list_test[i]
        item[i] = driver.find_element_by_css_selector('.er8xn')
        action = ActionChains(driver)
        item[i].clear()
        action.move_to_element(item).send_keys(body_text).perform()
        action.reset_actions()
        sleep(2)
    except:
        pass



