# email liuyibo906@163.com
# 时间 2022/12/21 21:36
#进制的显示数字
a=0b101
b=0x11
c=0o11
print(a)
print(b)
print(c)

print(bin(12))
print(oct(12))
print(hex(16))

#enumerate遍历列表
list1 = [1,2,3,4]
for index,value in enumerate(list1):
    print(index,value,end='|')
#while else   for else    break不会执行else   ,else是在循环正常结束执行

for i in range(10):
    if i==6:
        break
    print(i)
else:
    print('end of loop')