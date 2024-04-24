
str1 = 'itheima'
for i in str1:
    # 当某些条件成立退出循环 -- continue: 条件 i取到字符e
    if i == 'e':
        print('遇到e不打印')
        continue
    print(i)