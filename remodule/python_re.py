#正则表达式

import re
#普通字符
result=re.findall('P','Python')
print(result)

result=re.findall('o','i love Python')
print(result)

#预定义字符
#\d  数字
# \s 空白符、制表符、换行符
# \w  a-zA-Z0-9_
# \D 非数字   \S 非s   \W 非w
result=re.findall(r'\d','1234567890abcdefg')
print(result)

result=re.findall(r'\D','1234567890abcdefg')
print(result)

#元字符
#[]匹配一个字符，括号内的字符是或者的关系
result=re.findall(r'[123]','1234567890abcdefg')
print(result)
#^ 代表取反，放在中括号中
result=re.findall(r'[^123]','1234567890abcdefg')
print(result)
#- 代表区间
result=re.findall(r'[1-7]','1234567890abcdefg')
print(result)
#（）代表分组，返回分组的结果

result=re.findall(r'a[abc]','aaabacad')
print(result)

result=re.findall(r'a([abc])','aaabacad')
print(result)

#重复匹配

#{n}表示前面的字符重复n次
result=re.findall(r'\d{3}','1234567890abcdefg')
print(result)
#{n,m}标识前面的字符至少出现n次，至多出现m次
result=re.findall(r'\d{2,5}','1234567890abcdefg')
print(result)
#?表示非贪婪，默认是贪婪模式
result=re.findall(r'\d{2,5}?','1234567890abcdefg')
print(result)
#{n,} 前面的字符出现n次或任意次
result=re.findall(r'\d{2,}','1234567890abcdefg')
print(result)
#? 标识前面的字符出现0次或1次{0,1}
#+ 标识前面的字符至少出现一次
#* 标识前面的字符出现0次或任意次
#. 标识任意字符，不包含换行
#转义字符  \   匹配\*

#反向引用
wordstr='''
'hello' "python" 'love" 'peace"
'''
result=re.findall(r"['\"]\w+['\"]",wordstr)
print(result)


result=re.findall(r"('|\")(\w+)(\1)",wordstr)
print([x[1] for x in result])


#位置匹配

result=re.findall(r'\d{11}','15216772140')
print(result)

#^从开头开始  $结尾

result=re.findall(r'^\d{11}$','a15216772140s')
print(result)
