class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2

    return dummy.next


def buildLinkedList(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


nums1 = list(map(str, input().split(',')))
nums2 = list(map(str, input().split(','))) 

if nums1 == ['n'] and nums2 != ['n']:
    print(",".join(str(i) for i in nums2))
    
elif nums2 == ['n'] and  nums1 != ['n']:
    print(",".join(str(i) for i in nums1))
elif  nums2 == ['n'] and  nums1 == ['n']:
    print('n')




else:
   
    for i in nums1:
        i=int(i)
    for i in nums2:
        i=int(i)
    l1 = buildLinkedList(nums1)
    l2 = buildLinkedList(nums2)


    result = mergeTwoLists(l1, l2)
    c=[]

    while result:
       c.append(result.val)
       result = result.next
    print(",".join(str(i) for i in c))