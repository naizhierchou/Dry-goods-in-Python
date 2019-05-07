import re
match_obj = re.match("(qq):([1-9]\d{4,10})", "qq:10567")
if match_obj:
     print(match_obj.group())
     # 分组:默认是1⼀个分组，多个分组从左到右依次加1
     print(match_obj.group(1))
     # 提取第⼆个分组数据
     print(match_obj.group(2))
else:
     print("匹配失败")