# 1. 定义类 初始化属性 被烤和添加调料的方法 显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_static = '生的'
        # 调料列表
        self.condiments = []
    
    def cook(self, time):
        """烤地瓜的方法"""
        # 1. 先计算地瓜整体烤过的时间
        self.cook_time += time
        # 2. 用整体烤过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_static = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟
            self.cook_static = '半生不熟'
        elif 5 <= self.cook_time < 8:
            # 熟了
            self.cook_static = '熟了'
        if self.cook_time >= 8:
            # 烤糊了
            self.cook_static = '烤糊了'
    
    def __str__(self):
        return f'这个地瓜被考过的时间是{self.cook_time},状态是{self.cook_static},添加的调料有{self.condiments}'
    
    def add_condiments(self, condiment):
        # 用户意愿的调料追加到调料列表
        self.condiments.append(condiment)

# 2. 创建对象并调用相应的实例方法
digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
print(digua1)
digua1.cook(2)

digua1.add_condiments('胡椒粉')

print(digua1)
digua1.cook(2)
print(digua1)
digua1.cook(2)
print(digua1)