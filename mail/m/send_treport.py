from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from unittest_sample import unittest_test
import time
import os


# ==============定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')  # 邮箱服务器
    smtp.login("405641710@qq.com", "yzkbmzwadcombjif")  # 登录邮箱
    smtp.sendmail("405641710@qq.com", "1214706720@qq.com", msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(testresult):
    lists = os.listdir(testresult)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_dir = "D:\\Users\\lenovo\\Python_project\\ecshop\\testcase"
    test_report = "D:\\Users\\lenovo\\Python_project\\ecshop\\testresult"

    discover = unittest_test.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'w')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告