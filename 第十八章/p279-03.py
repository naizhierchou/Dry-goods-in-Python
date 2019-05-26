import re
# match_obj:该参数系统⾃动传⼊
def add(match_obj):
 # 获取匹配结果的数据
 value = match_obj.group()
 result = int(value) + 1
 # 返回值必须是字符串类型
 return str(result)
result = re.sub("\d+", add, "阅读数:10")
print(result)