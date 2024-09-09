n= int(input())
gas=list(map(int,input().split()))
dis=list(map(int,input().split()))
def passable(l1,l2):
    for i in range(len(l1)):
        if l1[i] < l2[i]:
            return 0
    return 1
for i in range(len(gas)):
    rest=[]
    a=gas[i]
    rest.append(a)
    for j in range(1,len(gas)):
        a=a+gas[(i+j)%n]-dis[(i+j-1)%n]
        rest.append(a)
    for j in range(len(rest)):
        




