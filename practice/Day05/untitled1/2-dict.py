d1 = {'name':'李磊','age':19,'heighyt':180,'weight':70}
'''
元素访问
1、获取：
    字典名[key]

'''
#增加键值对
d1["hobby"]=["quanli","jinqian","zhishi"]
print(d1)
#s删除键值对
d1.pop("age")
print(d1)

#遍历
'''
for key in d1:
    print(key)
'''

# 4、
for index,value in enumerate(d1):
    print(index,value)