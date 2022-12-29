# email liuyibo906@163.com
# 时间 2022/12/29 22:02
#使用__str__魔术方法可以打印对象时，打印返回值
class TranError(Exception):
    def __init__(self,errorcode=5000000,message='tranerror'):
        self.errorcode=errorcode
        self.message=message

    def __str__(self):
        return '%d,%s'%(self.errorcode,self.message)

if __name__ == '__main__':
    ts=TranError()
    print(ts)
