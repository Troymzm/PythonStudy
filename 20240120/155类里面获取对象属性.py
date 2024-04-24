class Washer():   # 大驼峰
    def wash(self):
        print('洗衣服')
    
    # 获取对象属性 self.属性名
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}') # type: ignore
        print(f'洗衣机的高度是{self.height}') # type: ignore

haier1 = Washer()

# 添加属性 对象名.属性名 = 值
haier1.width = 400 # type: ignore
haier1.height = 500 # type: ignore

# 对象调用方法
haier1.print_info()
