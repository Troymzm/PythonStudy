# 可变和不可变

# 1. 不可变  int 
#    1.1 声明变量保存整型数据 把这个数据赋值到另一个变量 id()检测两个变量的id值(内存的十进制值)

a = 1
b = a

print(b)

# 发现a和b的id值相同
print(id(a))
print(id(b))

# 修改a的数据测试id值
a = 2

print(b)

# 因为修改了a的数据 内存要开辟另外一份内存存储数据2 id检测a和b的地址是不同的
print(id(a))
print(id(b))


# 2. 可变类型  列表
aa = [10, 20]
bb = aa

print(bb)

print(id(aa))
print(id(bb))

aa.append(30)

print(aa)
print(bb)

print(id(aa))
print(id(bb))  # 列表是可变类型

"""
可变类型与不可变类型
1. 可变类型
列表 字典 集合
2. 不可变类型
整型 浮点型 字符串 元组
"""
