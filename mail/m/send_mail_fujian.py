import smtplib
from email.mime.text import MIMEText  # MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  # MIMEMulipart模块构造带附件

# 发送邮件的服务器
smtpserver = 'smtp.qq.com'

# 发送邮件用户和密码
user = '405641710@qq.com'
password = 'oozvllprlipjbjif'

# 发送者
sender ='405641710@qq.com'

# 接收者
receiver = '1214706720@qq.com'

# 邮件主题
subject = "附件的邮件"

# 发送附件
sendfile = open("E:\\qxlb.xlsx", "rb").read()

att = MIMEText(sendfile, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = "attachment;filename = 'qxlb.xlsx'"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()