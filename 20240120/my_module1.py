# 需求 一个函数 完成任意两个数字的加法运算
def testA(a, b):
    print(a + b)

# 测试信息
# testA(1, 1)
# __name__ 是系统变量 是模块的标识符 值是 如果是自身模块值是__main__  否则是当前模块的名字
if __name__ == '__main__':
    testA(1, 1)