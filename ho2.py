list1=[35,[3,2],23,56,32,"dd","abc",7.24,22,56,22,34,99,"dd",[3,2],[4,6],"ABc","abc",45,78,32,"a2c","abc"]
list2=list1.copy()
list3=[]
broad=[]
b1=0
lo=0
while lo< len(list1):
    a=list1[lo]
    b=list2[b1]    
    if type(list1[lo])==type(b)==int and a==b and lo!=b1:
        list3.append(lo)
        broad.append(a)
        lo+=1
        b1=0
    elif type(a)==type(b)==str and a.upper()==b.upper() and lo!=b1:
        list3.append(lo)   
        a=a.lower()
        broad.append(a)
        lo+=1
        b1=0
    elif type(a)==type(b)==list and lo!=b1:
        a.sort
        b.sort
        if a==b:
            list3.append(lo)
            broad.append(a)
        lo+=1
        b1=0
    else:
        b1+=1
    if b1==len(list2) :
        b1=0
        lo+=1
sw=[]
ge=0
while ge<len(broad): 
    sw.append(0)
    ge+=1
ge1=0
for i in broad:
    if broad.count(i)>1:
        sw[ge1]=i
    if sw.count(i)<2:
        print(i,"的重复次数是",broad.count(i),"次")
    ge1+=1
h=0
h1=0
while h<=len(broad):
    n=broad[h]
    if broad.count(n)>1:
        list3.remove(list3[h-h1])
        broad.remove(broad[h-h1])
        h1+=1
        h+=1
    else:
        h+=1
k=0
for i in list3:
    list1.pop(i-k)
    k+=1
print("去重后list为",list1)