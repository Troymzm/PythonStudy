class Washer():   # 大驼峰
    def wash(self):
        print('洗衣服')

haier1 = Washer()

# 添加属性 对象名.属性名 = 值
haier1.width = 40 # type: ignore
haier1.height = 50 # type: ignore

# 获取属性 对象名.属性名
print(f'洗衣机的宽度是{haier1.width}') # type: ignore
print(f'洗衣机的高度是{haier1.height}') # type: ignore