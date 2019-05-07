class Dog(object):
    def work(self): # ⽗类提供统⼀的⽅法，哪怕是空⽅法
        pass
class ArmyDog(Dog): # 继承 Dog
    def work(self): # ⼦类重写⽅法，并且处理⾃⼰的⾏为
        print('追击敌⼈')

class DrugDog(Dog):
     def work(self):
         print('追查毒品')

class Person(object):
     def work_with_dog(self, dog):
         dog.work()  # 使⽤⼩狗可以根据对象的不同⽽产⽣不同的运⾏效果, 保障了代码的稳定性

 # ⼦类对象可以当作⽗类来使⽤
dog = Dog()
print(isinstance(dog, Dog))  # isinstance 可以判断 dog 是否是 Dog 类的对象
ad = ArmyDog()
print(isinstance(ad, Dog))
dd = DrugDog()
print(isinstance(dd, Dog))
p = Person()
p.work_with_dog(dog)
p.work_with_dog(ad)  # 同⼀个⽅法，只要是 Dog 的⼦类就可以传递，提供了代码的灵活性
p.work_with_dog(dd)  # 并且传递不同对象，最终 work_with_dog 产⽣了不同的执⾏效果