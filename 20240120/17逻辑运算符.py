a = 0
b = 1
c = 2

# 1. and: 与：都真才真
print((a < b) and (c > b))
print(a > b and c > b)

# 2. or: 或: 一真则真，都假才假
print(a < b or c > b)
print(a > b or c > b)

# 3. not: 非: 取反
print(not False)

print(not c > b)

print(0 and 1)
print(1 and 2)  # 有0返回0，否则返回最后一个非零数字
print(2 and 1)

print(0 or 1)
print(1 or 2)  # 都为0返回0，否则返回第一个非零数字
print(2 or 1)