def func(name,age):
    print("my name is %s,I am %d years old"%(name,age))

#不定长参数
'''
def func(name,age,*hobby):
    print(name,age)
    print(hobby)

func("sunck",18,"power","money")

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(x=1,y=2,z=3,)
'''
#匿名函数
mySum2 = lambda a,b:a+b
print(mySum2(20,30))

#装饰器：是一个闭包，把一个函数作为参数传递，返回一个函数

#简单的装饰器
def myPrint():
    print("sunck is a good man")

def getNewPrint(func):
    def inner():
        print("-----------start")
        func()
        print("-----------end")
    return inner

myPrint = getNewPrint(myPrint)
myPrint()
#####################################################
def getAge(age):
    print("my age is %d years old"%age)

getAge(18)
getAge(-18)

def outer(func):
    def inner(age):
        if age < 0:
            func(0)
        else:
            func(age)
    return inner

#通用装饰器
