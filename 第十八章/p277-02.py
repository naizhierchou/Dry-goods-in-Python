import re
match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>hh</div>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
    match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")