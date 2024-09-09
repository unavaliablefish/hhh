liYu=[86,97,98,77,92,94,99,97]
liMa=[92,91,93,88,96,91,91,88]
liEn=[100,96,94,60,97,92,93,86]
liName=["太史慈","臧霸","张角","曹真","王朗","马谡","姜维","徐庶"]
def sa(a):
    sum=0
    for i in range(0,len(a)):
        sum+=a[i]
    b=float(sum/len(a))
    return b
def getmax(x):
    m=x[0]
    for i in range(0,len(x)):
        if x[i]>=m:
            m=x[i]
    c=x.index(m)
    return c
def cha(a,b):
    c=sa(a)
    d=sa(b)
    s=0
    for i in range(0,len(a)):
        s=(a[i]-c)*(b[i]-d)+s
    e=s/len(a)
    return e

print("语文课的平均成绩{},最高分姓名：{}".format(sa(liYu),liName[getmax(liYu)]))
print("数学课的平均成绩{},最高分姓名：{}".format(sa(liMa),liName[getmax(liMa)]))
print("英语课的平均成绩{},最高分姓名：{}".format(sa(liEn),liName[getmax(liEn)]))
print("语文与数学的协方差是",cha(liYu,liMa))
print("英语与数学的协方差是",cha(liEn,liMa))
print("语文与英语的协方差是",cha(liYu,liEn))

                   