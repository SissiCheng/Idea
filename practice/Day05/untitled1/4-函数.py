'''
认识函数：

    本质：对功能的封装
    优点：简化代码结构，增加代码复用度，

定义函数：
    def 函数名（参数列表）:
        语句
        reurn 表达式

调用函数：
函数名（参数列表）
本质：实参给形参赋值的过程
'''
#最简单的函数 （无参数，无返回）
def myPrint():
    print("i am a good girl")
    print("i am a very good girl")
    print ("i am a beautiful girl")
    print("i am a good girl")
myPrint();


def myFunc(name, age):
    print("我叫%s,我今年%d岁了"%(name,age))
