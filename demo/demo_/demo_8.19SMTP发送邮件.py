import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # MIMEMulipart模块构造带附件

user = '405641710@qq.com'
password = 'oozvllprlipjbjif'

# 发送者
sender = '405641710@qq.com'
# 接收者
receiver = "1214706720@qq.com"
# #①发送纯文本格式
# # msg = MIMEText('hello', 'plain', 'utf-8')
# #②发送html格式（可以直接把html字符串传入发送，也可以先保存读之后生成变量发送）
# # with open(r'C://Users//lenovo//Desktop//a.html','rb') as f:
# #     mail_body=f.read()
#
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>','html', 'utf-8')
#
# msg['Subject'] = Header("SMTP的问候", 'utf-8')
# msg['From']=Header('python 爱好者','utf_8')
# msg['To']=Header('管理员','utf_8')
# smtp = smtplib.SMTP('smtp.qq.com')
# # smtp.connect('smtp.qq.com')  # 邮箱服务器
# smtp.login(user, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()
# print("邮件已发出！注意查收")

#③发送带附件的邮件
# msg = MIMEMultipart()
# msg['Subject'] = "2019-08-19附件"
# msg['from']=sender
# msg['To']=Header('接收者','utf_8')
# smtp = smtplib.SMTP()
# smtp.connect('smtp.qq.com')
# # 邮件正文是MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#
# #构造附件att1
# att1 = MIMEText(open('111.jpg','rb').read(),"base64", "utf-8")
# att1["Content-Type"] = "application/octet-stream"
# # att1["Content-Disposition"] = "attachment;filename = 'testcase.html'"
# att1.add_header("Content-DIsposition","attachment",filename=("gbk","","老北京布鞋.jpg"))
# msg.attach(att1)
#
#
# #构造附件att2:
# att2=MIMEText(open('a.txt','r').read(),'base64','utf_8')
# att2["Content-Type"] = "application/octet-stream"
# # att1["Content-Disposition"] = "attachment;filename = 'testcase.html'"
# att2.add_header("Content-DIsposition","attachment",filename=("a.txt"))
# msg.attach(att2)

# smtp.login(user, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()

#④在正文中插入图片
msg=MIMEMultipart()
msg['Subject'] = "2019-08-19图片"
msg['from']=sender
msg['To']=Header('接收者','utf_8')
smtp = smtplib.SMTP('smtp.qq.com')
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:image0"></p>' +
    '</body></html>', 'html', 'utf-8'))
with open('blur.jpg','rb') as f:
    image=MIMEImage(f.read())
# 定义图片 ID，在 HTML 文本中引用
image.add_header('Content-ID','image0')
msg.attach(image)

smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print("邮件已发出！注意查收")


