a = 10
a += 1 # a = a + 1
print(a)

b = 10
b -= 1 # b = b - 1
print(b)

# 注意：先算复合赋值运算符右侧的表达式，再进行复合赋值运算
c = 10
c += 1 + 2  # c += 3
print(c)

d = 10
d *= 1 + 2  # d *= 3
print(d)
# += -= *= /= //= %= **=