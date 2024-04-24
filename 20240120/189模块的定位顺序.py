# 1. 自己的文件名不能和已有模块名重复 如果重复导致模块无法使用
import random
a = random.randint(1, 99)
print(a)


# 2. 当使用from 模块名 import 功能 导入模块的功能的时候 如果功能名字重复 导入的时候后定义或后导入的这个同名功能

# 拓展 名字重复
# import 模块名  不需要担心功能名字重复的问题
import time
print(time)

time = 1
print(time)

# 为什么变量能覆盖模块 -- 在Python中 数据是通过引用传递的