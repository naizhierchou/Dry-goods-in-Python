import re
# 匹配以数字开头的数据
match_obj = re.match("^\d.*", "3hello")
if match_obj:
     # 获取匹配结果
     print(match_obj.group())
else:
     print("匹配失败")