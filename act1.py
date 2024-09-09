def fre(nums, k):

    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num]+=1
        else:
            freq_map[num]=1

    sorted_nums = sorted(freq_map, key=freq_map.get, reverse=True)
 
    return sorted_nums[:k]


n = int(input())
nums = list(map(int, input().split()))
k = int(input())

result = fre(nums, k)
print(" ".join(map(str, sorted(result))))