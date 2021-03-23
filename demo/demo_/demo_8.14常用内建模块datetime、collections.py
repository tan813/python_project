#①datetime 模块
from datetime import timezone ,datetime,timedelta  # 导入datetime模块中datetime类
#获取当前时间
now=datetime.now()
print(now)
print(type(now))
#获取指定时间
dt=datetime(2019,8,14,14,27,12)
print(dt)

print('=======================================================================')
#timestamp
print(dt.timestamp())

t=1565764032.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

print('=======================================================================')
#str转换为datetime
cday = datetime.strptime('2019-08-14 14:39:00', '%Y-%m-%d %H:%M:%S')
print(cday)

print('=======================================================================')
#datetime转换为str
now=datetime.now()
print(now.strftime('%a %b %d %H:%M:%S'))

print('=======================================================================')
#datime加减
from datetime import  timedelta
now=datetime.now()
print(now)
print(now+timedelta(hours=1))
print(now+timedelta(days=1))
print(now+timedelta(days=1,hours=1))

print('=======================================================================')
#时区转换
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)# 拿到UTC时间，并强制设置时区为UTC+0:00:
print(utc_dt)
#astimezone()转换时区
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print('当前北京时间：%s'%bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('当前东京时间:%s'%tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('当前北京时间%s转换为东京时间:%s'%(bj_dt,tokyo_dt2))

print('=======================================================================')
#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，
# 均是str，请编写一个函数将其转换为timestamp：
import re
def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz_num=int(re.match('\w*\+(\d).*',tz_str).group(1))
    #创建时区
    tz_utc_5=timezone(timedelta(hours=tz_num))
    #加上时区时间
    utc_dt=dt.replace(tzinfo=tz_utc_5)
    return utc_dt.timestamp()
if __name__=='__main__':
    print(to_timestamp('2015-1-21 9:01:30','UTC+5:00'))




#②collections模块
from collections import  namedtuple,deque,defaultdict,Counter
#namedtuple创建自定义的tuple对象
Point=namedtuple('Point',['x','y'])#一个点的二维坐标
p=Point(1,2)
print(p.x)
print(p.y)

print('================================================================')
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
a=q.popleft()
print(q)
print(a)

print('================================================================')
dic=defaultdict(lambda:'NONE')#key值不存在返回默认值，创建对象时通过lambda函数传入
dic['key1'] = 'abc'
print(dic['key1'])
print(dic['key2'])

print('================================================================')
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
print(c)
print('================================================================')
# c=Counter('programming')
# print(c)

#③hashlib模块
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


print('================================================================')
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
# return hashlib.md5(s.encode('utf-8')).hexdigest()
def login(user, password):
    # md5=hashlib.md5()
    # md5.update(password.encode('utf-8'))
    # if md5.hexdigest()==db[user]:
    if hashlib.md5(password.encode('utf-8')).hexdigest()==db[user]:
        print('True')
    else:
        print('False')


if __name__=='__main__':
   login('michael', '123456')
   login('bob', 'abc999')
   login('alice', 'alice2008')
   login('michael', '1234567')
   login('bob', '123456')
   login('alice', 'Alice2008')
print('================================================================')

def get_md5(s):
   return hashlib.md5(s.encode('utf-8')).hexdigest()
def calc_md5(password):
    return get_md5(password + 'the-Salt')#ae4c852131dbe4f39ba4b5f53502d3a1

print(calc_md5('123456'))
print('================================================================')

import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    #user.password:数据库中密码 + salt 生成的 dist
    #get_md5(password + user.salt):用户待输入密码+salt生成的dist
    return user.password ==  get_md5(password + user.salt)

#测试
if __name__=='__main__':
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')