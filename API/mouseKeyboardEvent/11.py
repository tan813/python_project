from time import sleep, ctime

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print(ctime())
for i in range(10):
    try:
        el = driver.find_element_by_id("kw11")
        if el.is_displayed():
            break
    except Exception as e:
        # pass
        print(e)
        sleep(1)
else:
    print("time out")
print(ctime())
driver.quit()

driver.switch_to.p