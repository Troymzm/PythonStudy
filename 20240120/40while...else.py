# 需求：道歉五遍我错了，完成之后执行原谅你了
"""
1. 书写道歉的循环
2. 循环正常结束要执行的代码
"""
"""
语法：
while 条件:
    条件成立重复执行的代码
else:
    循环正常结束之后要执行的代码
"""
i = 1
while i <= 5:
    print('我错了')
    i += 1
else:
    print('原谅你了')