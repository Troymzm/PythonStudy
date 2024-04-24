mystr = "hello world and itcast and itheima and Python"

# 1. find()
print(mystr.find('and')) # 12
print(mystr.find('and', 15, 30)) # 23
print(mystr.find('ands')) # -1 子串不存在

# 2.index()
print(mystr.index('and')) # 12
print(mystr.index('and', 15, 30)) # 23
# print(mystr.index('ands')) 报错

# 3.count()
print(mystr.count('and')) # 3
print(mystr.count('and', 15, 30)) # 1
print(mystr.count('ands')) # 0

# rfind rindex 从右侧开始

# 4.rfind()
print(mystr.rfind('and')) # 35
print(mystr.rfind('ands')) # -1

# 5.rindex()
print(mystr.rindex('and')) # 35