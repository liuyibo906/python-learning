# email liuyibo906@163.com
# 时间 2022/12/27 22:13

#构造函数不能有返回值，

class Person:
    count=0
    def __init__(self,name,height):
        #构造函数
        #print('i am Person Object')
        self.__height=height  #实例属性，私有化变量,只能再类内部使用
        self.name=name
        __class__.count+=1

    def __say(self):  #私有化方法，类内部调用
        print('i am '+self.name)
        return 'HAHA'
    #装饰器调用函数时不需要括号   person.height
    @property
    def height(self):
        return self.__height
    def getheight(self):
        return self.__height
    def setheight(self,height):
        self.__height=height

    #类方法
    @classmethod
    def ClassSay(cls):
        print('共实例化对象'+str(cls.count)+'个')

person=Person('王平',180)
print(person.getheight())
print(person.setheight(160))
print(person.getheight())
print(person.height)