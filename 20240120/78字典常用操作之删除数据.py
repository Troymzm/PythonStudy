dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# del删除字典
# del(dict1)
# print(dict1)

# del删除指定的键值对, 若不存在则报错
del dict1['name']
print(dict1)

# clear()
dict1.clear()
print(dict1)