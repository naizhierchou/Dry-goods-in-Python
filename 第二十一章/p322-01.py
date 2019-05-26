# ############### 定义 ###############
class Pager:
     def __init__(self, current_page):
         # ⽤户当前请求的⻚码（第⼀⻚、第⼆⻚...）
         self.current_page = current_page
         # 每⻚默认显示10条数据
         self.per_items = 10
     @property
     def start(self):
         val = (self.current_page - 1) * self.per_items
         return val
     @property
     def end(self):
         val = self.current_page * self.per_items
         return val
# ############### 调⽤ ###############
p = Pager(1)
p.start # 就是起始值，即：m
p.end # 就是结束值，即：n