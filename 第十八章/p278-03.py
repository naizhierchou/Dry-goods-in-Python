import re
# 根据正则表达式查找数据，提示：只查找⼀次
# 1.pattern: 正则表达式
# 2.string: 要匹配的字符串
match_obj = re.search("\d+", "⽔果有20个 其中苹果10个")
if match_obj:
     # 获取匹配结果数据
     print(match_obj.group())
else:
     print("匹配失败")