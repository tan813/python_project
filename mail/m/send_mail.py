import smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱服务器
smtpserver='smtp.qq.com'
#发送邮箱用户/密码
user='405641710@qq.com'
password='oozvllprlipjbjif'
#发送邮箱
sender='405641710@qq.com'
#接收邮箱
receiver='1214706720@qq.com'
#发送邮件主题
subject='python email'
#编写html类型的邮件正文
msg=MIMEText('<HTML><H1>你好a</H1></HTML>','html','utf8')
msg['Subject']=Header(subject,'utf-8')
#连接发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()