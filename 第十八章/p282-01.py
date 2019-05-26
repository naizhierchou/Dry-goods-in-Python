import re
s="This is a number 234-235-22-423"
r=re.match(".+(\d+-\d+-\d+-\d+)",s)
r.group(1)

r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
r.group(1)