# 类 洗衣机 功能 洗衣服
# 1. 定义洗衣机类
class Washer():   # 大驼峰
    def wash(self):
        print('洗衣服')
        print(self)

haier = Washer()
print(haier)

haier.wash()

# 结论 由于打印对象和打印self得到的内容地址相同 所以self指的是调用该函数的对象