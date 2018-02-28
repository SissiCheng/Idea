

#try......expect.......else

try:
    print(10/0)
except(AttributeError,ZeroDivisionError) as e:
    print("产生了异常")
else:
    