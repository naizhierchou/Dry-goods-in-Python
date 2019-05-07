import re
match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com","hello@163.com")
if match_obj:
     print(match_obj.group())
     # 获取分组数据
     print(match_obj.group(1))
else:
     print("匹配失败")