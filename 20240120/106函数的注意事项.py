# 1. 使用一个函数  2. 测试注意事项
# 需求: 一个函数: 打印hello world

# 定义函数
def info_print():
    print('hello world')

# 调用函数
info_print()

"""
结论:
1. 函数先定义后调用, 如果先调用会报错
2. 如果没有调用函数, 函数里面的代码不会执行
3. 函数的执行流程: 当调用函数的时候, 解释器回到定义函数的地方去执行下方缩进的代码, 当这些代码执行完, 回到调用函数的地方继续向下执行, 定义函数的时候, 函数体内部缩进的代码并没有执行
"""