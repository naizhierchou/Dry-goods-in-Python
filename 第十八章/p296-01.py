import re
match_obj = re.match("hello\Sworld", "hello&world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")
match_obj = re.match("hello\Sworld", "hello$world")
if match_obj:
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")