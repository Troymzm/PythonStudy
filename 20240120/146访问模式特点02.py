"""
测试目标
1. r+ 和 w+ a+ 的区别: 
2. 文件指针对数据读取的影响
"""
# r+   r+没有该文件则报错  文件指针在开头  所以能读取出来数据
f = open('test.txt', 'r+')
con = f.read()
print(con)
f.close()

# w+  没有该文件则新建文件  文件指针在开头  用新内容覆盖原内容
f = open('test.txt', 'w+')
con = f.read()
print(con)
f.close()

# a+  没有该文件则新建文件  文件指针在结尾
f = open('test.txt', 'a+')
con = f.read()
print(con)
f.close()