name_list = ['Tom', 'Lily', 'Rose']

# 1. del
# del name_list 
# del(name_list)

# del 可以删除指定下标的数据
del name_list[0]
print(name_list)

name_list = ['Tom', 'Lily', 'Rose']
# 2. pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据
# 无论是按照下标还是删除最后一个，pop函数返回这个被删除的数据
del_name = name_list.pop()
print(del_name)
print(name_list)

del_name = name_list.pop(0)
print(del_name)
print(name_list)

name_list = ['Tom', 'Lily', 'Rose']

# 3. remove(数据) 移除列表中某个数据的第一个匹配项
name_list.remove('Rose')
print(name_list)

# 4. clear() -- 清空
name_list.clear()
print(name_list)