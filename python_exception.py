#异常处理，程序正常退出退出代码为 0,异常退出 退出代码为1
try:
    # b=10+a
    # c='1'+2
    a=int('abc')
    #a=1+2
except (NameError,TypeError) as e:
    print(e)
except Exception as e:
   # print(e)
    #捕获异常后跑出异常
    raise NameError('这是一个异常')
else:
    #未出现异常执行
    print('else')
finally:
    #始终执行
    print('finale')

print('2')
