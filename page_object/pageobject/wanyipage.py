from selenium.webdriver.common.by import By

from page_object.pageobject.basepage import BasePage


class WanyiPage(BasePage):
    # 定位器，通过元素属性定位元素
    username_loc = (By.ID,'auto-id-1610175453955') # 账号输入框
    password_loc = (By.ID,'auto-id-1610175453958')# 密码输入框
    login_loc= (By.ID,'dologin')#登录按钮
    name_loc = (By.ID,'1610178143817_dvGreetName') # 用户姓名
    js = "window.scrollTo(0,document.body.scrollHeight);"
    # 滑动到最底部
    def scroll(self):
        self.script(self.js)
    # 输入账号
    def input_username(self,username):
        iframes = self.driver.find_elements_by_tag_name('iframe')
        self.switch_frame(iframes[0])
        self.find_element(*self.username_loc).send_keys(username)
    # 输入密码
    def input_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)
    # 点击登录
    def click_login(self):
        self.find_element(*self.login_loc)
    #登录成功获取文本内容
    def get_name(self):
       return  self.find_element(*self.name_loc).text

