class Person(object):
    def feedCat(self,cat):
        cat.eat()
    def feedDog(self,dog):
        dog.eat()



class Animal(object):
    # def __init__(self,name):
    #     self.name=name
    # def eat(self):
    #     print("%s 吃"%self.name)
    def feedAnimal(self,animal):
        animal.eat()


class Cat(object):
    def __init__(self,name):
        super().__init__(name)

class Dog(object):
    def __init__(self,name):
        super().__init__(name)

dog1 = Dog("dog1")
cat1 = Cat("cat1")


per = Person()

