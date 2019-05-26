class ArmyDog(object):
    def bite_enemy(self):
        print('追击敌⼈')
class DrugDog(object):
    def track_drug(self):
        print('追查毒品')
class Person(object):
    def work_with_army(self, dog):
        dog.bite_enemy()
    def work_with_drug(self, dog):
        dog.track_drug()
ad = ArmyDog()
dd = DrugDog()
p = Person()
p.work_with_army(ad)
p.work_with_drug(dd)