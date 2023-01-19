import re
#三大查找方法

#findall 以列表的方式返回全部返回结果
#match 从开头开始匹配，匹配到结果返回,group()方法返回匹配结果
#search  字符串内查找。找到匹配就返回,不是从头查找，可以在字符串内查找

result=re.findall(r'\d{5}','13164564564641')
print(result)

result=re.search(r"\d{4}",'1234456464')
print(result.group())


result=re.match(r"\d{4}",'123466666')
print(result.group())


#split  分隔

print('1 2 3 4'.split(' '))
#
result=re.split('[\+\-\*\/]','1+2-3*4/5')
print(result)


#sub replace 替换,可以指定替换次数
myLine='i am hel, i am 40 years old,i like swiming!'
print(re.sub('i','I',myLine))
print(re.sub('i','I',myLine,2))


#分组group

result=re.match('h(.*)(\d{3})','hfasfdsfds2323adfasdf2323')
print(result.group())
print(result.group(0))
print(result.group(1))
print(result.group(2))


#反向引用和sub
myLine='i am Sniper, i am 40 years old,i like swiming!'
result=re.sub(r'(\w{3,})',r'<em>\1<em>',myLine)
print(result)


#flag 匹配模式  re.I 不区分大小写，re.S 忽略空格
print(re.findall(r"s\w{3,}", myLine,re.I))
