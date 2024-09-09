def findminpath(points):
        arr=[]
        n=len(points)
        
        for i in range(n):
            x1,y1=points[i][0],points[i][1]
            for j in range(i+1,n):
                x2,y2=points[j][0],points[j][1]
                arr.append([i,j,abs(x2-x1)+abs(y2-y1)])
        
        arr.sort(key=lambda x:x[2])
        
        parent=list(range(n))
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        
        edge=0
        cost=0
        for i,j,d in arr:
            a,b=find(i),find(j)
            if a!=b:
                parent[b]=a
                edge+=1
                cost+=d
            if edge==n-1:
                break
        return cost
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])


print(findminpath(points))

