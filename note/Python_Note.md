#### 基础语法

##### 条件和循环
Python- if:... elif:... else:

Python- for x in ... (take every element into x ,then carry out the function)
	ex:
		names = ['Machael','Bob','Tracy']
		for name in names:
			print(name)

Python-while

Python-dict
	ex: 
		d = ['Macheal':95,'Bob':75,'Tracy':85]

Python-set:
	ex:
		s= set([1,2,3])
##### 函数
Function:
	1.defination
	2.define:function name / parameter
		1.parameter kind check
		2.return
		3.if return several value ,it is a truple
	3.parameter:
		1.locayion parameter
		2.default parameter 
		3.variable parameter
		#4.**kw

	4.recursive function
##### 高级特性
切片 
?ex:
		L=['Micheal','Sarah','Tracy','Bob','Jack']

		r=[]
		n=3
		for i in range(n):
			r.append(L[i])

		r

		L[0:3]
		L[:3]
		L[1:3]
		L[-1]//倒数第一个数

		L[::5] //all element pick one from five
	ex:
		for ch in 'ABC':
			print(ch)

列表生成式
	ex:
		[x*x for x in range(1,11)]
		output;[1,4,9,16,25,36......]

		[m+n for m in 'ABC' for n in 'XYZ']

生成器 
	ex:
		def fib(max):
			n,a,b = 0,0,1
			while n < max:
				yield b
				a,b = b,a+b
				n = n+1
			return 'done'
迭代器：
	Iterable＃嚎傻韵?



迭代

##### Higher-order-function:
	take a function as parameter,this called higher order function

	map()
		ex:
			def f(x):
				return x*x
			r= mape(f,[1,2,3,4,5,6,7,8])
			list(r)

	reduce()
		ex:
			
              unction as return value

	filter()
		ex:
			
	sorted()
		ex:

return function:
	
匿名函数： lamda
装饰器：
偏函数：固定函数的某些参数


##### module

built-in function：
### 面向对象的程序设计
	<把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。>
	
### 类的定义 封装 实例化 调用

```
	class Student(object):
		pass
		
		
	class Student(object):
		def __init__(self, name, score):
			self.name = name
			self.score = score
	
```

### 访问限制
	```
	class Student(object):

		def __init__(self, name, score):
			self.__name = name
			self.__score = score
		
		def print_score(self):
			print('%s: %s' % (self.__name, self.__score))
	```
	
	
### 继承和多态

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

*“开闭”原则：*

对扩展开放：允许新增Animal子类；

对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
	```
class Animal(object):
	def run(self):
		print('Animal is running...')
	def run_twice(animal):
		animal.run()
		animal.run()
		
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

	```
### 获取对象信息
	type()
	```
	isinstance('a', str) 
	dir('ABC')
	```
##### 
## 面向对象高级编程

动态添加属性和方法

### 使用 __slots__
>   为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性:

``` 
__slots__ = ('name','age')

```
### 使用@property
后续再回顾


### 多重继承

### 定制类

### 枚举类

### 使用元类    
这部分我可能要弃疗了

##### logging
调试：
	--断言
	
### 读写文件
```
with open('/path/to/file', 'r') as f:
    print(f.read())
    
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
    
```


### stringIO/ByteIO
```
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'


>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...

```

## multiprocess
> 在Unix/Linux下，可以使用fork()调用实现多进程。

> 要实现跨平台的多进程，可以使用multiprocessing模块。

> 进程间通信是通过Queue、Pipes等实现的。

虽然目前并不明白这段是干啥用的

##### HTML
> HTML定义了页面的内容，CSS来控制页面元素的样式，而JavaScript负责页面的交互逻辑。