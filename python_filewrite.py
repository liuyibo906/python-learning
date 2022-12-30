# email liuyibo906@163.com
# 时间 2022/12/30 21:25
#r 只读，文件不存在报错
#w 写入，覆盖吸入,文件不存在创建
#a 写入，追加写入，文件不存在创建
#汉字写入按照utf_8,读取也是utf_8,默认时gbk

with open('write_data.txt','w',encoding='utf-8') as f:
    # datas=['my name','your name','family']
    # #会导致最后写入一个空行
    # #f.writelines([line+'\n' for line in datas])
    # f.write('\n'.join(datas))
    f.write('人生苦短，我用python')

with open('write_data.txt','r',encoding='utf-8') as f:
    print(f.read())