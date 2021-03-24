from time import sleep

from selenium.webdriver.common.by import By

from page_object.pageobject.basepage import BasePage


class BaiduPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    # kw_loc = (By.ID,'kw') #输入框
    kw_loc = ('id','kw')  # By.ID在By类中已经封装
    su_loc = (By.ID,'su') # 百度一下
    entrance_loc = (By.XPATH,'//*[@id="1"]/h3/a[1]') #网易邮箱登录官方入口

    # 打开百度
    def open(self):
        self._open(self.url,self.title)
    # 输入'网易邮箱登录'
    def input_login(self,content):
        self.find_element(*self.kw_loc).send_keys(content) #传实参kw_loc，形参content
    # 点击搜索
    def click_submit(self):
        self.find_element(*self.su_loc).click()
        sleep(2)
        assert self.checktitle('网易邮箱登录'),'搜索失败!'
    # 点击登录入口
    def click_entrance(self):
        self.find_element(*self.entrance_loc).click()
        self.switch_window()  # 有断言，所有在此处切换句柄
        sleep(2)
        assert self.checktitle('163网易免费邮'),'搜索失败!'

