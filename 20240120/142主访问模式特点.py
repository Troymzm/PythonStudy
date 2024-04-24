"""
测试目标
1. 访问模式对文件的影响
2. 访问模式对write()的影响
3. 访问模式是否可以省略
"""

# r: 如果文件不存在, 报错   不支持写入操作  表示只读
f = open('test.txt', 'r')
f.close()

# w: 只写 如果文件不存在 新建文件 执行写入 会覆盖原有内容
f = open('1.txt','w')
f.write('aaa')
f.close()

f = open('1.txt','w')
f.write('bbb')
f.close()

# a: 追加 如果文件不存在 新建文件 执行写入 会追加原有内容
f = open('2.txt','a')
f.write('aaa')
f.close()

f = open('2.txt','a')
f.write('bbb')
f.close()

# 访问模式可以省略 如果省略表示访问模式为r
f = open('2.txt')
f.close()