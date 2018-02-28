import math
import random

num1 = 10
num2 = num1
num3 = num4 = num5 = 104
num6,num7 = 6,7
print(num6,num7)

print(num1)
#数学函数
print(abs(-20))
print ((7>9)-(7<9))

print(max(1,2,3,4,5,6,7))
print(min(1,2,3,4,5,6,7))

#x的y次方
x=2
y=3
res = pow(x,y)
print(res)
print(round(10.9))#四舍五入
print(math.ceil(10.01))#向上取整
print(math.floor(10.999))#向下取整
print(math.modf(10.9))
print(math.sqrt(16))

#随机数
b = random.choice(1,2,4,7,9)
c = random.choice(range(5))#0-4
print(b)
#2 randrange[start,stop,step]
#3 random[0,1]#0-1随机浮点数
#4 uniform(2,5)
#5 shuffle #随机改变列表
random.shuffle(list)

