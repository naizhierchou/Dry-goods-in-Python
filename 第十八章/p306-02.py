import re
# pattern: 正则表达式
# repl: 替换后的字符串
# string: 要匹配的字符串
# count=0 替换次数，默认全部替换 , count=1根据指定次数替换
result = re.sub("\d+", "22", "评论数:10 赞数:20", count=1)
print(result)