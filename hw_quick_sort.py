counter1=0
counter2=0
li1=[3,44,38,5,47,15,36,26,27]
li2=[3,44,38,5,47,15,36,26,27]
print("orginal list:",li1)
def partitionHoare(list1,left,right):
    global counter1
    
    index=left
    pivot = list1[index]
    while True:
        while (left<right and list1[right] >= pivot):
            right-=1
        while (left<right and list1[left] <= pivot):
            left+=1
        if left>=right:
            break
        list1[left],list1[right]=list1[right],list1[left]
        counter1+=1
        right-=1
    list1[right],list1[index]=list1[index],list1[right]
    counter1+=1
    return right


def quick1(list3,left,right):
    if left<right:
        pivotindex = partitionHoare(list3, left, right)
        quick1(list3, pivotindex + 1, right)
        quick1(list3, left, pivotindex-1)
quick1(li1,0,8)

def partitionLomuto(list2,left,right):
    global counter2
    pivot=list2[right]
    target=left
    for i in range(left,right,1):
        if list2[i]<pivot:
            list2[target],list2[i]=list2[i],list2[target]
            target+=1
            counter2+=1
    list2[target],list2[right]=list2[right],list2[target]
    counter2+=1
    return target
def quick2(list4,left,right):
     if left<right:
        pivotindex = partitionLomuto(list4, left, right)
        quick1(list4, pivotindex + 1, right)
        quick1(list4, left, pivotindex-1)
quick2(li2,0,8)
print("hoare partition: swap times",counter1)
print("Lomuto partition: swap times",counter2)
print("sorted list:",li1)




    
