# email liuyibo906@163.com
# 时间 2022/12/27 23:05
from python_oop3 import  Person
class Student(Person):
    def __init__(self,name,height,stno,sch):
        #显示调用父类的构造函数
        super().__init__(name,height)
        self.stno=stno
        self.sch=sch

    def do_homeword(self):
        print(self.name+'在写作也')
    #重写，多态
    def say(self):
        print(self.name+'大声的说话')
    #静态方法
    @staticmethod
    def hello():
        print('这是一个静态方法')


student=Student('王小明','178','1000','解放录小学')
student.do_homeword()
student.run()
student.say()
