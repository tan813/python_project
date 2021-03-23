import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # MIMEMulipart模块构造带附件

user = '405641710@qq.com'
password = 'oozvllprlipjbjif'

# 发送者
sender = '405641710@qq.com'
# 接收者
receiver = {"240841985@qq.com", "1214706720@qq.com"}
class send_mail:

     def __init__(self,new_file):
         self.new_file=new_file

# 以html文本形式发
     def htmlmail(self):
         f = open(self.new_file, 'rb')
         mail_body = f.read()
         f.close()
         msg = MIMEText(mail_body, 'html', 'utf-8')
         msg['Subject'] = Header("自动化测试报告", 'utf-8')
         smtp = smtplib.SMTP()
         smtp.connect('smtp.qq.com')  # 邮箱服务器
         smtp.login(user, password)
         smtp.sendmail(sender, receiver, msg.as_string())
         smtp.quit()
         print("邮件已发出！注意查收")

# 以附件.html文件发
     def enclosuremail(self):
                # 发送附件
                f = open(self.new_file, 'rb')
                mail_body = f.read()
                f.close()

                att = MIMEText(mail_body, "base64", "utf-8")
                att["Content-Type"] = "application/octet-stream"
                # att["Content-Disposition"] = "attachment;filename = 'testcase.html'"
                att.add_header("Content-DIsposition","attachment",filename=("gbk","","测试结果.html"))
                msgRoot = MIMEMultipart('related')
                msgRoot['Subject'] = "测试报告附件"
                msgRoot.attach(att)
                smtp = smtplib.SMTP()
                smtp.connect('smtp.qq.com')
                smtp.login(user, password)
                smtp.sendmail(sender, receiver, msgRoot.as_string())
                smtp.quit()
                print("邮件已发出！注意查收")










