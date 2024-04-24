# 两个函数test A和test B -- 在A里嵌套调用B

# B函数
def testB():
    print('B函数开始------')
    print('这是B函数')
    print('B函数结束------')

# A函数
def testA():
    print('A函数开始------')
    #嵌套调用B
    testB()
    print('A函数结束------')

testA()