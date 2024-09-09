def numberToWords(num):
    if num == 0:
        return "Zero"
    
    # 辅助函数，将数字转换为英文表示
    def one(num):
        words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return words[num]

    def two_less_than_20(num):
        words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        return words[num]

    def ten(num):
        words = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        return words[num] 
    
    def helper(num):
        if num == 0:
            return ""
        elif num < 20:
            return two_less_than_20(num) + " "
        elif num < 100:
            return ten(num // 10) + " " + one(num % 10) + " "
        else:
            return one(num // 100) + " Hundred " + helper(num % 100)
    big_units = ["", "Thousand", "Million", "Billion"]

    result = ""
    unit_index = 0

    # 对数字按照千位分组，进行转换
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + big_units[unit_index] + " " + result
        num //= 1000
        unit_index += 1

    return result.strip()

# 读取输入
num = int(input().strip())

# 调用函数转换为英文表示并打印结果
print(numberToWords(num))