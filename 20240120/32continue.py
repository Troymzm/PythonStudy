# continue : 当条件成立，退出当前一次循环，继而执行下一次循环
# 吃5个苹果--循环：吃到第三个苹果吃出了虫子，第三个不吃了，没吃饱，继续吃--只有第三个没吃
i = 1
while i <= 5:
    if i == 3:
        print('吃出虫子了，这个不吃了')
        # 如果使用continue，在continue之前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1