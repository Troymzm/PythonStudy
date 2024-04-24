# 需求  一个函数有两个返回值1 2
# 不可以写成多个return
# 一个函数多个返回值的写法
def return_num():
    return 1, 2  # 返回值是元组

result = return_num()
print(result)

for i in result:
    print(i)

# return后面可以直接书写 元组 列表 字典 返回多个值
def return_num1():
    return (1, 2)  # 返回值是元组

def return_num2():
    return [1, 2]  # 返回值是列表

def return_num3():
    return {'age':30}  # 返回值是字典

result = return_num1()
print(result)

result = return_num2()
print(result)

result = return_num3()
print(result)