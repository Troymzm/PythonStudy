# NameError  print(num)   ZeroDivisionError  1/0
try:
    print(1/0)
except ZeroDivisionError:
    print('有错误')

# 如果尝试执行的代码的异常类型和要捕获的异常类型不一致 则无法正常捕获
# 一般try下方只放一行尝试执行的代码