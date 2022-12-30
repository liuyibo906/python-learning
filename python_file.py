# email liuyibo906@163.com
# 时间 2022/12/29 22:52
# file=open('data.txt','r')
# # print(file.readable())
# # # print(file.writable())
# #读取全部文件
# #data=file.read()
# #print(data)
# #读取前6个
# # data=file.read(6)
# # print(data)
# #移动光标
# # file.seek(7)
# # data=file.read()
# # print(data)
# #循环对行
# # data=file.readline()
# # while data:
# #     print(data,end='')
# #     data=file.readline()
# #读取多行
# datas=file.readlines()
# for line in datas:
#     print(line,end='')
# file.close()
#读取配置文件
configdata={}
with open('app.config','r') as file:
    datas=file.readlines()
    for line in datas:
        if line.startswith('#'):
            continue
        str=line.split('=')
        key=str[0]
        value=str[1].replace('\n','')
        configdata[key]=value

if __name__ == '__main__':
        print(configdata)