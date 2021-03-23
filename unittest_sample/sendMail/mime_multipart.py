import os
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ①设置邮箱域名、发件人邮箱、邮箱授权码、收件人邮箱
# smtp服务器:smtp.163.com
mail_host = 'smtp.163.com'

# 发件人邮箱
mail_sender = 'tanj3180@163.com'

# 邮箱登录授权码
mail_license = 'FDNXMSGLFPZNXRZZ'

# 收件人邮箱，可以为多个收件人
mail_receivers = '405641710@qq.com'
# ②构建多对象邮件对象
msg = MIMEMultipart()

# ③设置邮件头部内容
subject = 'python测试邮件'
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = 'Mr Tan<tanj3180@163.com>'
msg['To'] = mail_receivers

# 添加正文文本
mail_body = 'Hello,this is a test mail!'
msg1 = MIMEText(mail_body,'plain','utf-8')
msg.attach(msg1)

# 添加图片
with open("E:\\111.jpg",'rb') as f:
    mail_body = f.read()
msg2 = MIMEImage(mail_body)
msg2['Content-Disposition']='attachment;filename="shoe.png"'
msg.attach(msg2)

#添加附件
testreport = '../test_report'
# 列出目录的下所有文件和文件夹保存到lists
lists = os.listdir(testreport)
lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))  # 按时间排序


# 获取最新的文件路径保存到file_new
file_new = os.path.join(testreport, lists[-1])
# file_new = '../test_report/2020-12-15_23_03_04result.html'
with open(file_new,'rb') as f:
    mail_body = f.read()
msg3 = MIMEText(mail_body, 'text', 'utf-8')
msg3["Content-Type"] = "application/octet-stream"
msg3["Content-Disposition"] = "attachment;filename = testcase.html"
msg.attach(msg3)

# ④发送邮件
# 创建smtp对象
smtp = smtplib.SMTP()
# smtp.set_debuglevel(1)
# 设置发件人邮箱的域名和端口
smtp.connect(mail_host)
# 登录邮箱
smtp.login(mail_sender,mail_license)
# 发送邮件
smtp.sendmail(mail_sender,mail_receivers.split(','),msg.as_string())
print('邮件发送成功!')
smtp.quit()

# smtp :simple mail transfer protocol简单邮件传输协议
#MIME:muLtipurpose internet mail extensions