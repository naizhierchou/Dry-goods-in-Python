import re
# 匹配以数字结尾的数据
match_obj = re.match(".*\d$", "hello5")
if match_obj:
     # 获取匹配结果
     print(match_obj.group())
else:
     print("匹配失败")