# email liuyibo906@163.com
# 时间 2022/12/30 22:47
#1.创建连接 2、创建游标  3、执行脚本 4、关闭游标 5、关闭连接
import  sqlite3
#连接数据库
conn=sqlite3.connect('test.db')
#创建cursor
cur=conn.cursor()
#执行sql
#sql="insert into temp_lyb(id,name) values('2','syg')"
#sql='create table temp_lyb2(id int(10) primary key,name char(30))'
sql='select * from temp_lyb'
result=cur.execute(sql)
print(type(result))
print(result.fetchall())
#cur.execute(sql)
#关闭cursor
cur.close()
conn.commit()
#关闭连接
conn.close()
