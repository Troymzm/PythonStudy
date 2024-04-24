# 目标  定义init魔法方法设置初始化属性 并访问调用
"""
1. 定义类
    init魔法方法  width 和 height
    添加实例方法  访问实例属性

2. 创建对象
3. 验证成果
    调用实例方法
"""
class Washer():   # 大驼峰
    def __init__(self):  # 不需要手动调用
        self.width = 400
        self.height = 500
    
    # 获取对象属性 self.属性名
    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')

haier1 = Washer()
haier1.print_info()
