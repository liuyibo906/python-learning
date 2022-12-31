# email liuyibo906@163.com
# 时间 2022/12/31 11:34
#label 标签
from tkinter import  *
#创建窗口对象
root=Tk()
#设置标题
root.title("个人所得税APP")
#设置窗口大小,窗口便宜量据左和上
root.geometry("400x200+400+300")
#创建标签，在root容器中
inputLabel=Label(root,text='人生苦短，我用python',bg='lightblue',font='微软雅黑 12 normal')
#标签显示,填充X
inputLabel.pack(padx=5,pady=10,fill=X)

#创建标签，在root容器中
inputLabel=Label(root,text='人生苦短，我用python',bg='lightyellow',font='微软雅黑 12 normal')
#标签显示，填充xy,扩展到整个页面
inputLabel.pack(padx=5,pady=10,fill=BOTH,expand=True)
#创建窗口持续显示
root.mainloop()