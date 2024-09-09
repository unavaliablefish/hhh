a,b,c=map(int,input().split())
sum=a+b+c
print(sum) if (a<b+c)&(b<a+c)&(c<a+b) else print("不能组成三角形")