name_list = ['Tom', 'Lily', 'Rose']

name_list.append('xiaoming')
name_list.append([11, 22]) # type: ignore

print(name_list)

# 1. 列表是可变数据类型
# 2. append函数追加数据的时候如果数据是一个序列，追加整个序列到列表的结尾