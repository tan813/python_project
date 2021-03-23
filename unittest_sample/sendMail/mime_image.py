import smtplib

# ①设置邮箱域名、发件人邮箱、邮箱授权码、收件人邮箱
# smtp服务器:smtp.163.com
from email.header import Header
from email.mime.image import MIMEImage


mail_host = 'smtp.163.com'

# 发件人邮箱
mail_sender = 'tanj3180@163.com'

# 邮箱登录授权码
mail_license = 'FDNXMSGLFPZNXRZZ'

# 收件人邮箱，可以为多个收件人
mail_receivers = 'tanj3180@163.com'

# ②构建图片邮件对象
with open("E:\\111.jpg",'rb') as f:
    mail_body = f.read()
msg = MIMEImage(mail_body)
msg['Content-Disposition']='attachment;filename="shoe.png"'

# ③设置邮件头部内容
subject = 'python邮件测试'
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = 'ZhangSan<tanj3180@163.com>'
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