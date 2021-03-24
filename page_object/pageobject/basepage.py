from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self,driver,base_url,page_title):
        self.driver = driver
        self.url = base_url
        self.title = page_title

    # 检测title
    def checktitle(self,page_title):
        return page_title in self.driver.title # True or F
        # alse

    # 打开页面
    def _open(self,base_url,page_title):
        self.driver.get(base_url)
        self.driver.maximize_window()
        assert self.checktitle(page_title),'打开页面%s失败'%base_url

    # open()方法封装
    # def open(self):
    #     self._open(self.url,self.title) #传实参，调用_open()方法

    # 重写元素定位方法
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("页面中未能找到%s元素"%self)

    # 定义switch_frame方法切换框架
    def switch_frame(self,iframe):
        self.driver.switch_to.frame(iframe)

    # 定义switch_window方法切换句柄
    def switch_window(self):
        handles = self.driver.window_handles #获取所有页面句柄
        # self.driver.switch_to_window(handles[1])
        cur_handle = self.driver.current_window_handle # 获取当前页面句柄
        for handle in handles:
            if cur_handle != handle:
                self.driver.switch_to_window(handle)

    # 定义script方法，执行js脚本
    def script(self,src):
        self.driver.execute_script(src)

    # 重写send_keys方法
    # def send_keys(self,*loc,con):
    #     self.find_element(*loc).send_keys(con)