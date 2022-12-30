# email liuyibo906@163.com
# 时间 2022/12/30 22:47
#1.创建连接 2、创建游标  3、执行脚本 4、关闭游标 5、关闭连接
import pymysql
#连接数据库
conn=pymysql.connect(host='',user='',password='!',database='')
#创建cursor
cur=conn.cursor()
try:
    #执行sql
    #sql="insert into temp_lyb(id,name) values('2','syg')"
    #sql='create table temp_lyb2(id int(10) primary key,name char(30))'
    sql="select * from calc_work_hours where id=117"
    cur.execute(sql)
    result=cur.fetchall()
    print(type(result))
    print(result)
except Exception as e:
    pass
finally:
    #cur.execute(sql)
    #关闭cursor
    cur.close()
    #conn.commit()
    #关闭连接
    conn.close()
