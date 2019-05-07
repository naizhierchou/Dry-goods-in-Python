stus = [
 {"name": "zhangsan", "age": 18},
 {"name": "lisi", "age": 19},
 {"name": "wangwu", "age": 17}
]
func = lambda x: x['name']
stus.sort(key=func)
stus.sort(key = lambda x: x['age'])