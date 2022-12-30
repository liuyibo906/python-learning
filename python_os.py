# email liuyibo906@163.com
# 时间 2022/12/30 21:53
import os
print(os.getcwd())
if not os.path.exists('data'):
    os.mkdir('data')
else:
    os.rmdir('data')


print(os.listdir(os.getcwd()))

#遍历目录方法
for file in os.walk(os.getcwd()):
    print(file)