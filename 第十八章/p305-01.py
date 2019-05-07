import re
match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.youyong.cn</h1></html>")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")