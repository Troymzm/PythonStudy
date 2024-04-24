# 多继承 继承多个父类
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
class Prentice(School, Master):  # 如果子类和父类拥有同名属性和方法 子类创建对象调用属性和方法的时候 调用的是子类里面的同名属性和方法
    def __init__(self) -> None:
        self.kongfu = '[独创煎饼果子配方]'

    def make_cake(self):
        # 加初始化的原因 如果不加 属性值是上一次调用的init内的属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类调用父类的同名方法和属性 把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类函数.函数名(self)
        # 再次调用初始化的原因 这里想要调用父类的同名方法和属性 属性在init初始化位置 所以需要再次调用init
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 步骤 1. 创建类Tusun 用这个类创建对象 2. 用这个对象调用父类的属性和方法
class Tusun(Prentice):
    pass

daqiu = Tusun()
daqiu.make_cake()

daqiu.make_master_cake()
daqiu.make_school_cake()

daqiu.make_cake()