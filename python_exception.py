#异常处理，程序正常退出退出代码为 0,异常退出 退出代码为1
#调试DEBUG
from python_exceptions import  TranError
try:
    # b=10+a
    # c='1'+2
    a=1+2
    c=3*2
    b = int('abc')
    #raise TranError()
except (NameError,TypeError) as e:
    print(e)
except Exception as e:
    print(e)
    print(type(e))
    #捕获异常后跑出异常
else:
    #未出现异常执行
    print('else')
finally:
    #始终执行
    print('finale')

print('2')
