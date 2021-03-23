import time
from unittest_sample import unittest_test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class EcshopLogin(unittest_test.TestCase):
    def setUp(self):#此方法是执行用例之前的准备工作
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/ecshop/admin/privilege.php?act=login")
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//input[@value='进入管理中心']").click()
        #time.sleep(3)

#登录测试用例,必须以test开头
    def test_login(self):
        driver=self.driver;
         #进入框架
        driver.switch_to.frame("menu-frame")
        time.sleep(1)
        driver.find_element(By.LINK_TEXT,"商品列表").click()

        #出框架
        driver.switch_to.default_content()

        #进入框架
        driver.switch_to.frame("main-frame")
        #选择联想，，下拉框
        sel=Select(driver.find_element(By.NAME,"brand_id"))
        #sel=Select(driver.find_element_by_name("brand_id"))
         #sel.select_by_index("3") #通过下标
         #sel.select_by_value("9") #通过值
        sel.select_by_visible_text("联想")
        #点击搜索
        driver.find_element(By.CSS_SELECTOR,"input[value=' 搜索 ']").click()
        time.sleep(1)
         # 断言
         # assert driver.find_element(By.CSS_SELECTOR, "[href='privilege.php?act=logout']").text == "退出"
#增加商品测试用例
    def test_add_product(self):
        driver = self.driver;
        driver.switch_to.frame("menu-frame")
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "商品列表").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("main-frame")
#        assert driver.find_element(By.CSS_SELECTOR, "[href='goods.php?act=add']").text == "添加新商品"
        driver.find_element(By.LINK_TEXT,"添加新商品").click()
        driver.find_element(By.NAME,"goods_name").send_keys("老北京布鞋")
        sel=Select(driver.find_element_by_name("cat_id"))
        sel.select_by_value("14")
        driver.find_element(By.NAME,"shop_price").send_keys("4100")
        #文件上传
        driver.find_element(By.NAME,"goods_img_url").clear()
        driver.find_element(By.NAME,"goods_img_url").send_keys("E:\\111.jpg")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[value=' 确定 ']").click()
        time.sleep(1)
#删除商品测试用例
    def test_delete_product(self):
        driver = self.driver;
        driver.switch_to.frame("menu-frame")
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "商品列表").click()
        driver.switch_to.default_content()
        driver.switch_to.frame("main-frame")
        Array = driver.find_elements(By.NAME, "checkboxes[]")
        # for a in (0, 1, 2):
        Array[0].click()
        sel = Select(driver.find_element(By.ID, "selAction"))
        sel.select_by_value("trash")
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
    def tearDown(self):
      self.driver.quit()

if __name__=="__main__":#此方法是main方法，程序的入口
 unittest_test.main()
