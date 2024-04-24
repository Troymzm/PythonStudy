mystr = "hello world and itcast and itheima and Python"

# 1. replace() 把and换成he 有返回值 返回修改后的字符串 原有字符串数据并没有修改
new_str = mystr.replace('and', 'he')
print(new_str)
# 字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型

new_str = mystr.replace('and', 'he', 1)
print(new_str)

new_str = mystr.replace('and', 'he', 10) #替换次数如果超出子串出现的次数，表示替换所有子串
print(new_str)

# 2.split() -- 分割，返回一个列表，丢失分割字符
list1 = mystr.split('and')
print(list1)

list1 = mystr.split('and', 2)
print(list1)

# 3.join() -- 合并列表里面的字符串数据为一个大字符串
mylist = ['aa','bb','cc']

# aa...bb...cc
new_str = '...'.join(mylist)
print(new_str)