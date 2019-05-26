import re
match_obj = re.match("[^aeiou]", "h")
if match_obj:
     # 获取匹配结果
     print(match_obj.group())
else:
     print("匹配失败")