import os
import sqlite3
#①使用sqlite3数据库
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# cursor.execute('insert into user (id ,name) values (\'1\',\'Michael\')')
# cursor.execute('insert into user (id ,name) values (2, "Mike")')
# a=cursor.rowcount
# print(a)
# cursor.execute('select * from user where id=?',('1',))
cursor.execute('select * from user')
values=cursor.fetchall()
print(values)
cursor.close()
conn.commit()#提交事务
conn.close()


def get_score_in(low,high):
    try:
       L=[]
       cursor.execute('select name from student where score>=? and score<=? order by score',(low,high))
       values=cursor.fetchall()
       for value in values:
          L.append(value[0])
       return tuple(L)  # 列表转换成元组
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__=='__main__':
    #删除当前目录下已经存在的test.db文件，不会出现表已存在的情况
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    if os.path.isfile(db_file):
        os.remove(db_file)

    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # cursor.execute('drop table student')
    cursor.execute('create table student(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into student values('A-001','Adam',95)")
    cursor.execute(r"insert into student values('A-002','Bart',62)")
    cursor.execute(r"insert into student values('A-003','Lisa',78)")
    conn.commit()
    print(get_score_in(60,95))



#②使用mysql数据库
import mysql.connector
conn=mysql.connector.connect(user='root',password='admin',database='test')
cursor = conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('create table student(id varchar(20) primary key, name varchar(20), score int)')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.execute(r"insert into student values('A-001','Adam',95)")
cursor.execute(r"insert into student values('A-002','Bart',62)")
cursor.execute(r"insert into student values('A-003','Lisa',78)")

# 提交事务:
# conn.commit()
cursor.execute('select * from student where id=%s',('A-001',))#占位符%s
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()