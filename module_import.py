# email liuyibo906@163.com
# 时间 2022/12/28 22:45
#可以被导入的属性和方法
#包下可以添加一个__init__.py 文件，导入时执行
#pip list  查看已安装的包
#pip install  安装
#pip uninstall  卸载
__all__=['a','add']

a=10
b=20

def add(x,y):
    print(x+y)

class Kid:
    def __init__(self,age):
        self.age=age
    def say(self):
        print('我今年'+str(self.age)+'岁')