timestr = input ("请输入一个时间")
#12：12：34
timearr = timestr.split("：")
h = eval(timearr[0])
m = eval(timearr[1])
s = eval(timearr[2])

s += 1
if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h ==24:
            h = 0
print(str(h)+":"+str(m)+":"+str(s))