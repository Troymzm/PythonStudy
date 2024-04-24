# 师傅类
class Master(object):
    def __init__(self) -> None:
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 学校类
class School(object):
    def __init__(self) -> None:
        self.kongfu = '[新式煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 徒弟类
class Prentice(School, Master): 
    def __init__(self) -> None:
        self.kongfu = '[独创煎饼果子配方]'
        self.money = 2000000
        self.__money = 2000000  # 私有属性 无法继承
    
    # 定义函数 获取私有属性值 get_xx
    def get_money(self):
        return self.__money
    
    # 定义函数 修改私有属性值 set_xx
    def set_money(self):
        self.__money = 500
    
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class Tusun(Prentice):
    pass

daqiu = Tusun()

print(daqiu.money)
print(daqiu.get_money())
daqiu.set_money()
print(daqiu.get_money())