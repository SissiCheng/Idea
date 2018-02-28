class Addobj(object):
    def sum(self,a,b):
        return a + b

class Subobj(object):
    def sub(self,a,b):
        return a-b

class Calculator(Addobj,Subobj):
    pass

c = Calculator()
print(c.sum(1,2))
print(c.sub(5,4))