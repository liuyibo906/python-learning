# email liuyibo906@163.com
# 时间 2022/12/27 22:13
# class ClassDemo:
#     pass
#
#
# myclass=ClassDemo()
# myclass1=ClassDemo()
# print(myclass)
# print(myclass1)
# print(type(myclass))
# print(hex(id(myclass)))


#构造函数不能有返回值，

class Person:
    count=0
    def __init__(self,name,height):
        #构造函数
        #print('i am Person Object')
        self.__height=height  #实例属性
        self.name=name
        __class__.count+=1

    def say(self):
        print('i am '+self.name)
        return 'HAHA'
    #类方法
    @classmethod
    def ClassSay(cls):
        print('共实例化对象'+str(cls.count)+'个')

person=Person('王平',180)
Person.ClassSay()
#person1=Person()
# person.__init__()
print(person.say())
# print(person.height)
# print(person1.height)
# print(Person.height)
# print(person.__dict__)  #所有实例都有方法，查看属性和方法