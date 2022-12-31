# email liuyibo906@163.com
# 时间 2022/12/31 11:48
from tkinter import  *
from tax_caclate import  calc_taxamount
def tax_calc():
    inputcount=inputvalue.get()
    tax=calc_taxamount(int(inputcount))
    outputvalue.set("个人所得税金额是:%.2f" % tax)

#创建窗口对象
root=Tk()
#设置标题
root.title("个人所得税APP")
#设置窗口大小,窗口便宜量据左和上
root.geometry("400x200+400+300")
#容器,将多个框体封装在一起,容器显示在主窗口对象中
topFrame=Frame(root)
#创建标签，在root容器中
inputLabel=Label(topFrame,text='请输入月收入：')
#标签显示,填充X
inputLabel.pack(side=LEFT, padx=5,pady=5)
#单行输入文本
inputvalue=StringVar()
inputentry=Entry(topFrame,textvariable=inputvalue)
inputentry.pack(side=LEFT,padx=5,pady=5)

#创建按钮，command 执行函数的名称
inputbutton=Button(topFrame,text='计算',command=tax_calc)
inputbutton.pack(side=LEFT,padx=5,pady=5)

topFrame.pack(padx=5,pady=5)
#创建输出
outputvalue=StringVar()
outputvalue.set('点击计算')
outputlabel=Label(root,textvariable=outputvalue,font='微软雅黑 24 normal',fg='blue')
outputlabel.pack(padx=5,pady=5)

root.mainloop()