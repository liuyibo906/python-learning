# email liuyibo906@163.com
# 时间 2022/12/27 21:46
#可变参数*，表示可以传入一个元组

def print_food(*food,placeno,waiter):
    print('这是底'+placeno+'的菜')
    for f in food:
        print(f)
    print('服务员是:'+waiter)


#print_food('饺子','饮料','12','小王')
#必须使用关键字参数方式调用方法,print函数就是可变参数
print_food('饺子','饮料',placeno='12',waiter='小王')


#局部变量和全局变量   global 定义全局变量