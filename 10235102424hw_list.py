list1=[35,[3,2],23,56,32,'dd','abc',7.24,22,56,22,34,99,'dd',[3,2],[4,6],'ABc','abc',45,78,32,'a2c','abc']
list2=list1.copy()
list3=[]
list4=[]
for i in list2:
    if type(i)==str:
        a=i.lower()
        list3.append(a)
    elif type(i)==list:
        i.sort
        list3.append(i)
    else:
        list3.append(i)
print("去重后的列表为：".format(list3))
for j in list3:
    if j not in list4:
        list4.append(j)
print(list4)
for k in list4:
    b=list3.count(k)
    if b>1:
        print(k,"的重复次数是{}次".format(b))


            
            


           
           

