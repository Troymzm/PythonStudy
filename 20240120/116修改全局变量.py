# B函数想要a的取值是200
a = 100

print(a)

def testA():
    print(a)

def testB():
    a = 200  # 如果直接修改a=200, 此时的a是局部变量
    print(a)

testA()
testB()

print(a)

def testC():
    global a # 声明a是全局变量
    a = 200  # 如果直接修改a=200, 此时的a是局部变量
    print(a)

testC()

print(a)

"""
总结:
    1. 如果在函数里面直接把变量a=200赋值, 此时的a不是全局变量的修改, 而是相当于在函数内部声明了一个新的局部变量
    2. 函数体内部修改全局变量: 先global声明a为全局变量, 然后再变量重新赋值
"""