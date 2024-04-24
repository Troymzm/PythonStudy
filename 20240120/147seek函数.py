"""
语法 文件对象.seek(偏移量, 起始位置) 0 开头 1 当前 2 结尾
目标
    1. r 改变文件指针位置 改变读取数据开始位置或把文件指针放在结尾(无法读取数据)
    2. a 改变文件指针位置 做到可以读取出来数据
"""

f = open('test.txt', 'r+')
# 改变读取数据开始位置
f.seek(2 , 0)
con = f.read()
print(con)
f.close()

f = open('test.txt', 'r+')
# 把文件指针放在结尾(无法读取数据)
f.seek(0 , 2)
con = f.read()
print(con)
f.close()

# a 改变文件指针位置 做到可以读取出来数据
f = open('test.txt', 'r+')
# 把文件指针放在开头且不偏移
f.seek(0 , 0)
con = f.read()
print(con)
f.close()

f = open('test.txt', 'r+')
# 把文件指针放在开头且不偏移
f.seek(0)
con = f.read()
print(con)
f.close()