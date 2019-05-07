import re
match_obj = re.match("<([a-zA-Z1-6]+)><([a-zA-Z1-6]+)>.*</\\2></\\1>", "<html><h1>www.youyong.cn</h1></html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")