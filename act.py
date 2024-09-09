def bubble_sort(arr):
    a=[]
    n = len(arr)
    for i in range(n):
        b=arr
        a.append(b)
        # 标志位，用于检测是否发生了交换
        swapped = False
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有发生交换，说明数组已经有序，提前结束
        if not swapped:
            break
    return a

# 测试
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("排序后的数组:", sorted_arr)