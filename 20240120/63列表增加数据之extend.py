name_list = ['Tom', 'Lily', 'Rose']

name_list.extend('xiaoming')
name_list.extend(['xiaoming', 'xiaohong'])

print(name_list)

# 1. 列表是可变数据类型
# 2. extend函数追加数据的时候如果数据是一个序列，拆开逐一追加到结尾