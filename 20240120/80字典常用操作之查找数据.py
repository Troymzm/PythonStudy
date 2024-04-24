dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 1. [key]
print(dict1['name'])  # 返回对应的值(key存在),key不存在则报错
# 2. 函数
# 2.1 get()
print(dict1.get('name'))
print(dict1.get('names'))  # 如果key不存在, 返回None
print(dict1.get('names','Lily'))  # 返回Lily
print(dict1)
# 2.2 keys() -- 查找字典中所有的key, 返回可迭代的对象
print(dict1.keys())

# 2.3 values() -- 查找字典中所有的value值, 返回可迭代的对象
print(dict1.values())

# 2.4 items() -- 查找字典中所有的键值对, 返回可迭代的对象, 里面的数据是元组, 元组数据1是字典的key, 元组数据2是字典的value
print(dict1.items())