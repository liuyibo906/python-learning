# email liuyibo906@163.com
# 时间 2022/12/21 21:36
# 进制的显示数字
a = 0b101
b = 0x11
c = 0o11
print(a)
print(b)
print(c)

print(bin(12))
print(oct(12))
print(hex(16))

# enumerate遍历列表
list1 = [1, 2, 3, 4]
for index, value in enumerate(list1):
    print(index, value, end='|')
# while else   for else    break不会执行else   ,else是在循环正常结束执行

for i in range(10):
    if i == 6:
        break
    print(i)
else:
    print('end of loop')

# 字符串分割,返回列表
a = '1,2,3,4,5'
print(a.split(','))

# 连接,使用#连接字符串和列表
a = '#'
print(a.join('234'))
print(a.join(['1', '2', '3', '4', '5']))

# 查找,rindex 从右查找   startswith 以什么开头,endswith 以什么结尾 strip， lstrip,rstrip  去除字符串
a = '#he#llo#'
print(a.find('l'))
print(a.find('ll'))
print(a.index('l'))
print(a.startswith('h'))
print(a.strip('#'))
print(a)
# 格式化
print('这个是一个%08d' % 10)
print('这个是一个%05.2f' % 1.666)
print('这个是{:,.2f}'.format(10000))  # 千分位

# 编码 encode   解码 decode
a = '人生苦短，我用python'
print(a.encode().decode())

# 正则表达式
import re

b = '800012'
g = '15216772140'
print(re.match(r"^8\d{5}$", b))
print(re.match(r"^1[3456789]\d{9}$", g))
