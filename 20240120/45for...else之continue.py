# continue退出当前一次循环后else后面的代码正常执行
str1 = 'itheima'
for i in str1:
    if i == 'e':
        continue
    print(i)
else:
    print('循环正常结束执行的else的代码')