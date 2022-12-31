# email liuyibo906@163.com
# 时间 2022/12/31 12:12
def calc_taxamount(income):
    if income<=5000:
        tax=0
    elif income<8000:
        tax=(income-5000)*3/100
    elif income<=17000:
        tax=3000*3/100+(income-5000-3000)*0.1
    else:
        tax=income*45/100
    return tax
if __name__ == '__main__':
    print(calc_taxamount(30000))