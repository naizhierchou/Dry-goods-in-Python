import re
match_obj = re.match("^\d.*\d$", "4hello4")
if match_obj:
     # 获取匹配结果
     print(match_obj.group())
else:
     print("匹配失败")