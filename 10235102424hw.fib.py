count=0
def getfib(n):
    global count
    count+=1
    if n==1:
        
        return 0
    elif n==2:
        
        return 1
    else:
        
        return getfib(n-1)+getfib(n-2)
def getsfib(n,list1):
    global cou
    cou+=1
    if list1[n]!= 0:
        return list1[n]                
    else:
        if n>=2:
            list1[n]=getsfib(n-1,list1)+getsfib(n-2,list1)
        elif n==1: 
            list1[1]=1
            list1[0]=0
        elif n==0:
            list1[0]=0
        return list1[n]
cou=0
n=int(input("please input a number:"))
for i in range(1,n+1):
    print(getfib(i),end=" ")
print("\n")
print("total:",count)
print("\n")
print("优化后")
list1=[0]*(n+1)

getsfib(n,list1)
for i in range(0,n,1):        
    print(list1[i] ,end=' ')
print("\n")
print("total:",cou)
