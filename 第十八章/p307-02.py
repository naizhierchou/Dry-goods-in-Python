import re
my_str="貂蝉,杨⽟环,⻄施,王昭君"
# 1. 正则
# 2. 要匹配的字符串
# maxsplit=1 分割次数， 默认全部分割
result = re.split(",|:", my_str, maxsplit=1)
print(result)