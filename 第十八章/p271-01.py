import re
# 匹配⾮特殊字符中的⼀位
match_obj = re.match("\w", "A")
if match_obj:
     # 获取匹配结果
     print(match_obj.group())
else:
     print("匹配失败")