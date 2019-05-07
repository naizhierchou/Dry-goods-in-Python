# ############### 定义 ###############
class Goods:
     @property
     def price(self):
        return "laowang"
# ############### 调⽤ ###############
obj = Goods()
result = obj.price # ⾃动执⾏ @property 修饰的 price ⽅法，并获取⽅法的返回值
print(result)