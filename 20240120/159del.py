class Washer():   # 大驼峰
    def __init__(self, width, height):  # 不需要手动调用
        self.width = width
        self.height = height
    
    def __del__(self):  # 不需要手动调用
        print('对象已经删除')

haier1 = Washer(10, 20)
