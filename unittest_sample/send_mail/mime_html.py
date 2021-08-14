import smtplib

# ①设置邮箱域名、发件人邮箱、邮箱授权码、收件人邮箱
# smtp服务器:smtp.163.com
from email.header import Header
from email.mime.text import MIMEText

mail_host = 'smtp.163.com'

# 发件人邮箱
mail_sender = 'tanj3180@163.com'

# 邮箱登录授权码
mail_license = 'FDNXMSGLFPZNXRZZ'

# 收件人邮箱，可以为多个收件人
mail_receivers = '405641710@qq.com'

# ②构建文本邮件对象
file_new = '../test_report/2020-12-15_23_03_04result.html'
with open(file_new,'rb') as f:
    mail_body = f.read()
msg = MIMEText(mail_body, 'html', 'utf-8')



# ③设置邮件头部内容
subject = 'python邮件测试'
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = mail_sender
msg['To'] = mail_receivers
# ④发送邮件
# 创建smtp对象
smtp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口
smtp.connect(mail_host)
# 登录邮箱
smtp.login(mail_sender,mail_license)
# 发送邮件
smtp.sendmail(mail_sender,mail_receivers,msg.as_string())
print('邮件发送成功!')
smtp.quit()