# 定义⼀个列表保存，姓名、性别、职业
nameList = ['xiaoZhang', '男', '⽊匠'];
# 当修改职业的时候，需要记忆元素的下标
nameList[2] = '铁匠'
# 如果列表的顺序发⽣了变化，添加年龄
nameList = ['xiaoWang', 18, '男', '铁匠']
# 此时就需要记忆新的下标，才能完成名字的修改
nameList[3] = 'xiaoxiaoWang'
