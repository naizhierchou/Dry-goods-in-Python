a=0
b=1
c=3

#and运算，只要有一个值为0 则结果为0，否则结果为最后一个非0 数字
a and b #0
b and a #0
c and b #1
b and c #3

#or运算，只有所有值为0，结果才为0，否则结果为第一个非0数字
a or a #0
a or b #1
b or a #1
c or b #3
b or c #1