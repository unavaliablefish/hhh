a=int(input(""))
b=list(map(int,input("").split(" ")))
for i in range(len(b)-1):
    if(b[i]>b[i-1] and b[i]>b[i+1]):
        print(i)

