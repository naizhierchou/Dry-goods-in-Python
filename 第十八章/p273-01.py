import re
match_obj = re.match("https?", "http")
if match_obj:
 print(match_obj.group())
else:
 print("匹配失败")