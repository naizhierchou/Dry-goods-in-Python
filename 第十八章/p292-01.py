#coding=utf-8
import re
ret = re.match(".","M")
print(ret.group())
ret = re.match("t.o","too")
print(ret.group())
ret = re.match("t.o","two")
print(ret.group())