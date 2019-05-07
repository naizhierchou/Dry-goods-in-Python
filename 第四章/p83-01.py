info = {'name':'班⻓','age':18}
print(info['age']) # 获取年龄
# print(info['sex']) # 获取不存在的key，会发⽣异常
print(info.get('sex')) # 获取不存在的key，获取到空的内容，不会出现异常
print(info.get('sex'， '男')) # 获取不存在的key, 可以提供⼀个默认值。