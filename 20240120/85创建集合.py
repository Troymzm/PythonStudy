# 1. 创建有数据的集合
s1 = {10, 20, 30, 40, 50}
print(s1)  # 集合没有顺序, 不支持下标
s2 = {40, 20, 10, 20, 30}
print(s2)  # 集合中没有重复元素
s3 = set('abcdefg')
print(s3)
# 2. 创建空集合: 只能用set()
s4 = set()
print(s4)
print(type(s4))

s5 = {}  # 创建空字典
print(type(s5))