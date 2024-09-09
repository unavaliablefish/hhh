def findKthLargest(nums, k) :
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index],nums[right] = nums[right],nums[pivot_index]
            store_index = left
            for i in range(left,right):
                if nums[i] < pivot:
                    nums[store_index],nums[i] = nums[i],nums[store_index]
                    store_index +=1
            nums[right],nums[store_index] = nums[store_index],nums[right]
            return store_index           
        
        def quickselect(left, right, k_smallest):
            if left==right:
                return nums[left]
            pivot_index = (left+right)//2
            pivot_index = partition(left,right,pivot_index)
            if pivot_index == k_smallest:
                return nums[k_smallest]
            elif pivot_index<k_smallest:
                return quickselect(pivot_index+1,right,k_smallest)
            else:
                return quickselect(left,pivot_index-1,k_smallest)
            
        
        
        return quickselect(0, len(nums) - 1, len(nums) - k)
n = int(input())
nums = list(map(int,input().split()))
k=int(input())
print(findKthLargest(nums,k))






