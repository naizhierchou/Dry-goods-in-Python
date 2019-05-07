import re
# 匹配特殊字符中的⼀位
match_obj = re.match("\W", "&")
if match_obj:
     # 获取匹配结果
     print(match_obj.group())
else:
     print("匹配失败")