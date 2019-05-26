import re
# 如果hello的⾸字符⼩写，那么正则表达式需要⼩写的h
ret = re.match("h","hello Python")
print(ret.group())
# 如果hello的⾸字符⼤写，那么正则表达式需要⼤写的H
ret = re.match("H","Hello Python")
print(ret.group())
# ⼤⼩写h都可以的情况
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())
# 匹配0到9第⼀种写法
ret = re.match("[0123456789]Hello Python","7Hello Python")
print(ret.group())
# 匹配0到9第⼆种写法
ret = re.match("[0-9]Hello Python","7Hello Python")
print(ret.group())
ret = re.match("[0-35-9]Hello Python","7Hello Python")
print(ret.group())
# 下⾯这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python","4Hello Python")
# print(ret.group())