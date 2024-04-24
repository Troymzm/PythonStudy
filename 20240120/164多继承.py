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
class Prentice(School, Master):  # 默认继承第一个父类的同名属性和方法
    pass

daqiu = Prentice()

print(daqiu.kongfu)

daqiu.make_cake()