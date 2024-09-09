# 本实验目的：
# 1.掌握布尔代数的基本运算原理：与，或，非，异或  
# 2.掌握半加器的原理
# 参考 https://www.weixueyuan.net/a/368.html
##########################################
# 1.异或门实现单位加法
#
##########################################
num1=0b0   #0b开头的数字代表是2#数字
num2=0b0
sum=num1 ^ num2  #异或
print(num1,"加",num2,"的和是:",sum)

num1=0b1
num2=0b0
sum=num1 ^ num2 #异或
print(num1,"加",num2,"的和是:",sum)

num1=0b0
num2=0b1
sum=num1 ^ num2 #异或
print(num1,"加",num2,"的和是:",sum)
##########################################
# 2.异或门+与门实现半加器
#
##########################################
num1=0b1
num2=0b1
sum=num1 ^ num2 #异或
print(num1,"加",num2,"的和是:",sum)
carry=num1 & num2 #与
print(num1,"加",num2,"的和是:",carry,sum)