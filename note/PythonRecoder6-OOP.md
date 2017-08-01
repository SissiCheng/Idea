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





	