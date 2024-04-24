try:
    print(1/0)
except (ZeroDivisionError, NameError):
    print('有错误')