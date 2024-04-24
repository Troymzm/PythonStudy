# continue退出当前一次循环后else后面的代码正常执行
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print('我错了')
    i += 1
else:
    print('原谅你了')