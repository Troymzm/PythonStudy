class Washer():   # 大驼峰
    def __init__(self):  # 不需要手动调用
        self.width = 100
    
    def __str__(self):
        return '解释说明: 类的说明或对象状态的说明'

haier1 = Washer()
print(haier1)
