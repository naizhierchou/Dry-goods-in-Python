import re
# 空格属于空⽩字符
match_obj = re.match("hello\sworld", "hello world")
if match_obj:
     result = match_obj.group()
     print(result)
else:
     print("匹配失败")
# \t 属于空⽩字符
match_obj = re.match("hello\sworld", "hello\tworld")
if match_obj:
     result = match_obj.group()
     print(result)
else:
     print("匹配失败")