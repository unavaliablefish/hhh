a=int(input(""))
b=map(int,input("").split(" "))
c=int(input(""))
if c in b:
    d=b.index(c)
    print(d)
else:
    print(-1)

