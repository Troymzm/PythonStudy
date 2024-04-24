# break终止循环后else后面的代码不执行
i = 1
while i <= 5:
    if i == 3:
        break
    print('我错了')
    i += 1
else:
    print('原谅你了')