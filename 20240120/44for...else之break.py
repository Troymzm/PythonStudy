# break终止循环后else后面的代码不执行
str1 = 'itheima'
for i in str1:
    if i == 'e':
        break
    print(i)
else:
    print('循环正常结束执行的else的代码')