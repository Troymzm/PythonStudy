for i in range(1, 10, 1):
    print(i)  # 从1开始不包括10, 步长为1
for i in range(1, 10):
    print(i)  # 从1开始不包括10, 省略步长默认为1
for i in range(1, 10, 2):
    print(i)  # 从1开始不包括10, 步长为2
for i in range(10):
    print(i)  # 默认从0开始不包括10, 省略步长默认为1

# range(start, end, step)
# 1. 如果不写开始, 默认从0开始
# 2. 如果不写步长, 默认为1