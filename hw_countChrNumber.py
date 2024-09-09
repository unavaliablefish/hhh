a=input('请输入字符串：')
other=0
o=""
num=0
n=""
up=0
u=""
low=0
l=""
for i in a:
    b=ord(i)
    if b>31 and b<48 or b>57 and b<65 or b>90 and b<97 or b>122 and b>127:
        other+=1
        o=o+" {}".format(i)
    elif b>47 and b<58:
        num+=1
        n=n+' {}'.format(i)
    elif b>64 and b<91:
        up+=1
        u=u+' {}'.format(i)
    elif b>96 and b<123:
        low+=1
        l=l+' {}'.format(i)
    else:
        print("请输入正规字符")
if other>=num and other>=up and other>=low:
    print('其他种类最多，分别为{}'.format(o))
elif num>=up and num>=low:
    print('数字种类最多，分别为{}'.format(n))
elif up>=low:
    print('大写字母种类最多，分别为{}'.format(u))
else:
    print('小写字母种类最多，分别为{}'.format(l))
