def findmin(l1):
    min=l1[0]
    for i in range(len(l1)):
        if l1[i] < min:
            min = l1[i]
    return min
def distance(l1,l2):
    return abs(l1[0]-l2[0])+abs(l1[1]-l2[1])
def findminsum(loc):
    visited=[False]*len(loc)
    dic={}
    k=len(loc)
    for i in range(k):
        if visited[i]:
            continue
        else:
            dis=[]
            for j in range(k):
                dis.append(distance(loc[i]),loc[k])
            for 





