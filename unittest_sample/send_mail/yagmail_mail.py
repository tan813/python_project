import yagmail

yag = yagmail.SMTP(user = 'tanj3180@163.com',password='FDNXMSGLFPZNXRZZ',host='smtp.163.com')
# 收件人
receiver = '405641710@qq.com'
# 主题
subject = 'Yagmail test mail'
# 正文
contents = 'This is a python test mail!'
# 附件
file1 = '../test_report/2020-12-15_23_03_04result.html'
file2 = 'E:\\111.jpg'
attachments= [file1,file2]
yag.send(receiver,subject,contents,attachments)
print('邮件发送成功!')