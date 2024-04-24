name_list = ['Tom', 'Lily', 'Rose']

# 1. 修改指定下标的数据
name_list[0] = 'aaa'
print(name_list)

# 2. 逆序 reverse()
list1 = [1, 3, 2, 5, 4, 6]
list1.reverse()
print(list1)

# 3. sort() 排序:升序和降序 默认升序
list1.sort()
print(list1)

list1.sort(reverse=False) # 升序
print(list1)

list1.sort(reverse=True)  # 降序
print(list1)