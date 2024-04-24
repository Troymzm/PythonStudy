try:
    f = open('test1.txt', 'r')
except Exception as result:
    f = open('test1.txt', 'w')
else:
    print('没有异常')
finally:  # 无论是否异常都要执行的代码
    f.close()