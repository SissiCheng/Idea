### �������ĳ������
	<�Ѽ����������Ϊһ�����ļ��ϣ���ÿ�����󶼿��Խ����������󷢹�������Ϣ����������Щ��Ϣ������������ִ�о���һϵ����Ϣ�ڸ�������֮�䴫�ݡ�>
	
### ��Ķ��� ��װ ʵ���� ����

```
	class Student(object):
		pass
		
		
	class Student(object):
		def __init__(self, name, score):
			self.name = name
			self.score = score
	
```

### ��������
	```
	class Student(object):

		def __init__(self, name, score):
			self.__name = name
			self.__score = score
		
		def print_score(self):
			print('%s: %s' % (self.__name, self.__score))
	```
	
	
### �̳кͶ�̬

�̳п��԰Ѹ�������й��ܶ�ֱ���ù����������Ͳ���������������ֻ��Ҫ�����Լ����еķ�����Ҳ���԰Ѹ��಻�ʺϵķ���������д��
��̬���Ե�Ѽ�������ص�����˼̳в���̬���������Ǳ���ġ�

*�����ա�ԭ��*

����չ���ţ���������Animal���ࣻ

���޸ķ�գ�����Ҫ�޸�����Animal���͵�run_twice()�Ⱥ�����
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
### ��ȡ������Ϣ
	type()
	```
	isinstance('a', str) 
	dir('ABC')
	```





	