import re
# ⽔果列表
fruit_list = ["apple", "banana", "orange", "pear"]
# 遍历数据
for value in fruit_list:
     # | 匹配左右任意⼀个表达式
     match_obj = re.match("apple|pear", value)
     if match_obj:
        print("%s是我想要的" % match_obj.group())
     else:
        print("%s不是我要的" % value)