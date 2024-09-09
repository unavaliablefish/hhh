a=int(input("please input a number:"))
count=0
if a==1:
    print("无素数")
if a==2:
   print(2)
if a==3 or a==4:
    print(2)
    print(3)
if a==5:
    print(2)
    print(3)
    print(5)
if a>5:
    print(2)
    print(3)
    for i in range(5,a,2):
        b=0
        for j in range(3,i,2):
            count+=1
            if i%j==0:
               b=1
        if b==0:
           print(i)
print("count:",count)

