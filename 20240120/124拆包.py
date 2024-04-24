# 1. 拆包元组数据
def return_num():
    return 100, 200

num1, num2 = return_num()
print(num1)
print(num2)

# 2. 拆包字典数据
# 先准备字典 然后拆包
dict1 = {'name': 'Tom', 'age': 20}
# dict1中有两个键值对 拆包的时候用两个变量接收数据
a, b = dict1
print(a)
print(b)

# v值
print(dict1[a])
print(dict1[b])