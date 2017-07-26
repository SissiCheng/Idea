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